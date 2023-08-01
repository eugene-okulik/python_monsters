import requests


def prepare_post():
    header = {'Content-Type': 'application/json'}
    my_data = {
        "title": "titlekajshdfoiquweyfkjahsdkfjhqewf",
        "body": "bodykasjdhiwuyetjhsdkjdvgh",
        "userId": 42
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=my_data, headers=header).json()
    return response['id']


def del_a_post(post_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


def get_all_posts():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100, 'Not all posts returned by API'


def get_one_post():
    post_id = prepare_post()
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    print(response[1])
    del_a_post(post_id)


def add_post():
    header = {'Content-Type': 'application/json'}
    # my_data = json.dumps({
    #     "title": "titlekajshdfoiquweyfkjahsdkfjhqewf",
    #     "body": "bodykasjdhiwuyetjhsdkjdvgh",
    #     "userId": 42
    # })
    my_data = {
        "title": "titlekajshdfoiquweyfkjahsdkfjhqewf",
        "body": "bodykasjdhiwuyetjhsdkjdvgh",
        "userId": 42
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=my_data, headers=header).json()
    print(response)


def put_post():
    header = {'Content-Type': 'application/json'}
    my_data = {
        "title": "titlekajshdfoiquweyfkjahsdkfjhqewf-UPD",
        "body": "bodykasjdhiwuyetjhsdkjdvgh-UPD",
        "userId": 42
    }
    response = requests.put('https://jsonplaceholder.typicode.com/posts/42', json=my_data, headers=header).json()
    print(response)


def patch_post():
    header = {'Content-Type': 'application/json'}
    my_data = {
        "title": "titlekajshdfoiquweyfkjahsdkfjhqewf-UPD"
    }
    response = requests.patch('https://jsonplaceholder.typicode.com/posts/42', json=my_data, headers=header).json()
    print(response)


def delete_post():
    post_id = 42
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    requests.delete(url)
    response = requests.get(url)
    assert response.status_code == 404, 'Post is not deleted'


get_one_post()
