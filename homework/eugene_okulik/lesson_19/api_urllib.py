from urllib import request, error
import json


def get_all_posts():
    req = request.Request('https://jsonplaceholder.typicode.com/posts')
    response = request.urlopen(req)
    # print(json.loads(response.read().decode('utf-8'))[0])
    response = json.load(response)
    assert len(response) == 100, 'Not all posts returned by API'


def get_one_post():
    req = request.Request('https://jsonplaceholder.typicode.com/posts/42')
    response = request.urlopen(req)
    # print(json.loads(response.read().decode('utf-8'))[0])
    print(json.load(response))


def add_post():
    req = request.Request('https://jsonplaceholder.typicode.com/posts', method='POST')
    req.add_header('Content-Type', 'application/json')
    # req.add_header('Authorization', 'Bearer sdlfkjgslkdfjglskjdflkjsdf')
    req.data = json.dumps(
        {
            "title": "titlekajshdfoiquweyfkjahsdkfjhqewf",
            "body": "bodykasjdhiwuyetjhsdkjdvgh",
            "userId": 42
        }
    ).encode('ascii')
    response = json.load(request.urlopen(req))
    print(response)


def put_post():
    req = request.Request('https://jsonplaceholder.typicode.com/posts/42')
    req.method = 'PUT'
    req.add_header('Content-Type', 'application/json')
    req.data = json.dumps(
        {
            "title": "titlekajshdfoiquweyfkjahsdkfjhqewf-UPD",
            "body": "bodykasjdhiwuyetjhsdkjdvgh-UPD",
            "userId": 3
        }
    ).encode('ascii')
    response = json.load(request.urlopen(req))
    print(response)


def patch_post():
    req = request.Request('https://jsonplaceholder.typicode.com/posts/42')
    req.method = 'PATCH'
    req.add_header('Content-Type', 'application/json')
    req.data = json.dumps(
        {
            "title": "titlekajshdfoiquweyfkjahsdkfjhqewf-UPD",
            "userId": 3
        }
    ).encode('ascii')
    response = json.load(request.urlopen(req))
    print(response)


def delete_post():
    post_id = 101
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    req = request.Request(url, method='DELETE')
    json.load(request.urlopen(req))
    req = request.Request(url)
    # response = request.urlopen(req).read()
    try:
        request.urlopen(req).read()
    except error.HTTPError as err:
        assert err.code == 404
        return
    assert False, f'Post {post_id} is not deleted'


delete_post()
