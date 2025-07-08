import pytest

from generator import generate_user_data
from helper import create_user, login_user, get_ingredients

@pytest.fixture
def user_data():
    return generate_user_data()

@pytest.fixture
def registered_user(user_data):
    response = create_user(user_data)
    assert response.status_code == 200, f"Failed to create user: {response.text}"
    yield {
        "data": user_data,
        "response": response
    }

@pytest.fixture
def auth_token(registered_user):
    credentials = {
        "email": registered_user["data"]["email"],
        "password": registered_user["data"]["password"]
    }
    login_response = login_user(credentials)
    assert login_response.status_code == 200, f"Login failed: {login_response.text}"
    return login_response.json()["accessToken"]

@pytest.fixture
def ingredients():
    try:
        ingredients_data = get_ingredients()
        assert len(ingredients_data) > 0, "No ingredients received"
        return [ingredient["_id"] for ingredient in ingredients_data[:2]]
    except Exception as e:
        pytest.fail(f"Failed to get ingredients: {str(e)}")

@pytest.fixture(autouse=True)
def cleanup(request):
    yield
    if "registered_user" in request.fixturenames:
        # Здесь должна быть очистка данных, если API поддерживает удаление
        pass