import unittest
import requests
import sys


class TestGetPostsWithoutPrep(unittest.TestCase):

    def test_get_all_posts(self):
        response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100)


class TestGetPosts(unittest.TestCase):
    post_id = None

    def setUp(self):
        header = {'Content-Type': 'application/json'}
        my_data = {
            "title": "titlekajshdfoiquweyfkjahsdkfjhqewf",
            "body": "bodykasjdhiwuyetjhsdkjdvgh",
            "userId": 42
        }
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=my_data, headers=header).json()
        print('created', response['id'])
        self.post_id = response['id']

    def tearDown(self) -> None:
        print(f'Deleting post {self.post_id}')
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')

    def test_get_one_post(self):
        post_id = self.post_id
        print('testing', post_id)
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
        print(response)
        self.assertEqual(post_id, response['id'])

    @unittest.skip('Bug #234234')
    def test_simple(self):
        self.assertEqual(1, 1)

    @unittest.skipIf(sys.platform.startswith('lin'), 'not working on linux')
    def test_simple2(self):
        print(sys.platform)
        self.assertEqual(2, 2)


'''
assertEqual(a, b) — a == b
assertNotEqual(a, b) — a != b
assertTrue(x) — bool(x) is True
assertFalse(x) — bool(x) is False
assertIs(a, b) — a is b
assertIsNot(a, b) — a is not b
assertIsNone(x) — x is None
assertIsNotNone(x) — x is not None
assertIn(a, b) — a in b
assertNotIn(a, b) — a not in b
assertIsInstance(a, b) — isinstance(a, b)
assertNotIsInstance(a, b) — not isinstance(a, b)
assertGreater(a, b) — a > b
assertGreaterEqual(a, b) — a >= b
assertLess(a, b) — a < b
assertLessEqual(a, b) — a <= b
'''