import allure
import pytest
from helper import create_user



@allure.feature("Создание пользователя")
class TestCreateUser:
    @allure.title("Успешное создание пользователя")
    def test_create_user_success(self, user_data):
        with allure.step("Создать нового пользователя"):
            response = create_user(user_data)

        with allure.step("Проверить статус код и ответ"):
            assert response.status_code == 200
            assert response.json()["success"] is True

    @allure.title("Создание существующего пользователя")
    def test_create_existing_user(self, registered_user):
        existing_user = registered_user["data"]
        with allure.step("Попытаться создать существующего пользователя"):
            response = create_user(existing_user)

        with allure.step("Проверить ошибку"):
            assert response.status_code == 403
            assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, user_data, missing_field):
        invalid_data = user_data.copy()
        del invalid_data[missing_field]

        with allure.step(f"Создать пользователя без поля {missing_field}"):
            response = create_user(invalid_data)

        with allure.step("Проверить ошибку"):
            assert response.status_code == 403
            assert response.json()["success"] is False