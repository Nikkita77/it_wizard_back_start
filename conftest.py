import pytest
from faker import Faker


@pytest.fixture
def generate_user():
    fake = Faker("ru_RU")
    return {
        "login": fake.user_name(),
        "email": fake.email(),
        "password": fake.password()

    }


@pytest.fixture
def set_url():
    return "http://5.63.153.31:5051/v1/account"


@pytest.fixture
def headers():
    return {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }
