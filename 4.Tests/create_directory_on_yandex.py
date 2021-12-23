import requests


def create_directory(token, directory_name):
    URL = 'https://cloud-api.yandex.net/v1/disk/resources/'
    resp = requests.get(
        url=URL,
        params={'path': f'disk:/{directory_name}'},
        headers={'Authorization': f'OAuth {token}'}
    )
    if resp.status_code == 200:
        print('Такая папка уже существует')
        return
    resp = requests.put(
        url=URL,
        params={'path': f'disk:/{directory_name}'},
        headers={'Authorization': f'OAuth {token}'}
    )
