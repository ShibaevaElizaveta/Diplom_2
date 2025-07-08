import allure

from helper import create_order


@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_auth_with_ingredients(self, auth_token, ingredients):
        with allure.step("Создать заказ с авторизацией"):
            response = create_order(auth_token, ingredients)

        with allure.step("Проверить успешное создание"):
            assert response.status_code == 200
            assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации с ингредиентами")
    def test_create_order_no_auth_with_ingredients(self, ingredients):
        with allure.step("Создать заказ без авторизации"):
            response = create_order(ingredients=ingredients)

        with allure.step("Проверить успешное создание"):
            assert response.status_code == 200
            assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients(self, auth_token):
        with allure.step("Создать заказ без ингредиентов"):
            response = create_order(auth_token)

        with allure.step("Проверить ошибку"):
            # API возвращает 400 Bad Request
            assert response.status_code == 400
            assert "Ingredient ids must be provided" in response.json().get("message", "")

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredients(self, auth_token):
        invalid_ingredients = ["invalid_id1", "invalid_id2"]
        with allure.step("Создать заказ с неверными ингредиентами"):
            response = create_order(auth_token, invalid_ingredients)

        with allure.step("Проверить ошибку сервера"):
            # API возвращает 500 Internal Server Error
            assert response.status_code == 500