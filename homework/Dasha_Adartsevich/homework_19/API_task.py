import requests


def get_token_for_user():
    user_name = {"name": "Dasha"}
    response = requests.post('http://167.172.172.115:52355/authorize', json=user_name).json()
    return response['token']


def check_if_token_is_alive():
    user_token = get_token_for_user()
    response = requests.request('GET', f'http://167.172.172.115:52355/authorize/{user_token}').text
    print(response)


def get_all_memes():
    token = get_token_for_user()
    header = {'Authorization': f'{token}'}
    response = requests.request('GET', 'http://167.172.172.115:52355/meme', headers=header).json()
    print(response)


get_token_for_user()
check_if_token_is_alive()
get_all_memes()