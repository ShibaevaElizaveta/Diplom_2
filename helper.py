import requests
from data import BASE_URL, Endpoints


def create_user(user_data):
    response = requests.post(
        f"{BASE_URL}{Endpoints.CREATE_USER}",
        json=user_data
    )
    return response


def login_user(credentials):
    response = requests.post(
        f"{BASE_URL}{Endpoints.LOGIN}",
        json=credentials
    )
    return response


def get_ingredients():
    response = requests.get(
        f"{BASE_URL}{Endpoints.INGREDIENTS}"
    )
    return response.json()["data"]


def create_order(auth_token=None, ingredients=None):
    headers = {"Authorization": auth_token} if auth_token else {}
    payload = {"ingredients": ingredients} if ingredients else {}

    response = requests.post(
        f"{BASE_URL}{Endpoints.CREATE_ORDER}",
        headers=headers,
        json=payload
    )

    return response