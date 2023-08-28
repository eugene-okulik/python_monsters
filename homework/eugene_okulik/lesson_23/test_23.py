import requests
import pytest
import sys


@pytest.fixture(scope='function')
def post_id():
    header = {'Content-Type': 'application/json'}
    my_data = {
        "title": "titlekajshdfoiquweyfkjahsdkfjhqewf",
        "body": "bodykasjdhiwuyetjhsdkjdvgh",
        "userId": 42
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=my_data, headers=header).json()
    print('created', response['id'])
    yield response['id']
    print(f'Deleting post {response["id"]}')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{response["id"]}')


@pytest.fixture(scope='session')
def print_smth():
    print('Before all')
    yield
    print('After all')


def test_get_all_posts(print_smth):
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100, 'Not all posts returned by API'


def test_get_one_post(post_id, count):
    print('testing', post_id, count)
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    assert post_id == response['id']


@pytest.mark.skip(reason='Bug #12345')
def test_1(print_smth):
    assert 1 == 1


@pytest.mark.skipif(sys.platform.startswith('lin'), reason='not working on windows')
def test_2():
    assert 2 == 2


@pytest.mark.smoke
def test_3():
    assert 2 == 2


@pytest.mark.parametrize('data', [(8, 1), (7, 2), (6, 3)])
def test_4(data):
    a, b = data
    assert a + b == 9


@pytest.mark.one
@pytest.mark.parametrize('data', [('user1', 'qwer1'), ('user2', 'qwer2'), ('user3', 'qwer3')])
def test_5(data):
    login, password = data
    print(login, password)
