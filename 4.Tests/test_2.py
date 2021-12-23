import requests
import unittest
from create_directory_on_yandex import create_directory


class TestSomething(unittest.TestCase):
    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_check_directory_1(self):
        TOKEN = 'token'
        directory_name = 'test_vgdfs'
        create_directory(TOKEN, directory_name)
        URL = 'https://cloud-api.yandex.net/v1/disk/resources/'
        resp = requests.get(
            url=URL,
            params={'path': f'disk:/{directory_name}'},
            headers={'Authorization': f'OAuth {TOKEN}'}
        )
        self.assertEqual(resp.status_code, 200)

    def test_check_directory_2(self):  # True, если ошибка
        TOKEN = '123'
        directory_name = 'test_vgdfs'
        create_directory(TOKEN, directory_name)
        URL = 'https://cloud-api.yandex.net/v1/disk/resources/'
        resp = requests.get(
            url=URL,
            params={'path': f'disk:/{directory_name}'},
            headers={'Authorization': f'OAuth {TOKEN}'}
        )
        self.assertNotEqual(resp.status_code, 200)
        if resp.status_code == 401:
            print('Не авторизован')
        elif resp.status_code == 400:
            print('Некорректные данные.')
        else:
            print('Другая ошибка')
