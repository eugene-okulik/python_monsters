from locust import task, HttpUser
import random
from requests import exceptions as req_exceptions


class QuickStartUser(HttpUser):
    token = None
    meme_ids = []

    def on_start(self):
        response = self.client.post('/authorize', json={"name": "Eugeny"})
        self.token = response.json()['token']

    @task
    def get_all_memes(self):
        self.client.get(
            '/meme',
            headers={'Authorization': self.token}
        )

    @task
    def post_a_meme(self):
        rnd = random.randrange(432, 4567)
        body = {
            "text": "skdjfhksjdfhksjdfhskdf",
            "url": "slkdfksdhfksjdhkfjsdfh",
            "tags": ["tag1"],
            "info": {"key1": "val1"}
        }
        response = self.client.post('/meme', json=body, headers={'Authorization': self.token})
        # if response.status_code == 200:
        print(response.text)
        try:
            with open('log.txt', 'a') as log_file:
                log_file.write(response.json()['id'])
            self.meme_ids.append(response.json()['id'])
        except req_exceptions.JSONDecodeError:
            pass

    def on_stop(self):
        for meme_id in self.meme_ids:
            self.client.delete(f'/meme/{meme_id}', headers={'Authorization': self.token})
