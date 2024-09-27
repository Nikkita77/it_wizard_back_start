import pytest
import requests
from client import Client

from conftest import generate_user

@pytest.fixture
def client():
    return Client()

data = [
    # Короткий логин
    {
        "login": "1",
        "email": "ivan@mail.ru",
        "password": "1314254"
    },

    # Короткий емайл
    {
        "login": "12134",
        "email": "e",
        "password": ""
    },
    # Короткий пароль
    {
        "login": "12134",
        "email": "ivan@mail.ru",
        "password": "d"
    }
]


def test_post_v1(set_url, generate_user, headers):
    response = requests.request("POST", set_url, headers=headers, json=generate_user)

    print(response.text)


def test_post_v2(set_url, generate_user, headers):
    print(generate_user)
    response = requests.request("POST", set_url, headers=headers, json=generate_user)
    print(response.text)


@pytest.mark.parametrize("data", data)
def test_invalid_post_v2(data, client):
    print(generate_user)
    response = client.register_user(data)
    print(response.text)
