import allure

from helper import login_user


@allure.feature("Авторизация пользователя")
class TestLoginUser:
    @allure.title("Успешный логин")
    def test_login_success(self, registered_user):
        credentials = {
            "email": registered_user["data"]["email"],
            "password": registered_user["data"]["password"]
        }
        with allure.step("Выполнить вход"):
            response = login_user(credentials)

        with allure.step("Проверить успешную авторизацию"):
            assert response.status_code == 200
            assert "accessToken" in response.json()

    @allure.title("Логин с неверными данными")
    def test_login_invalid_credentials(self, registered_user):
        invalid_credentials = {
            "email": registered_user["data"]["email"],
            "password": "invalid_password"
        }
        with allure.step("Выполнить вход с неверными данными"):
            response = login_user(invalid_credentials)

        with allure.step("Проверить ошибку авторизации"):
            assert response.status_code == 401
            assert response.json()["message"] == "email or password are incorrect"