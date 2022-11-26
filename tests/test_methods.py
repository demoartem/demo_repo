import allure
from framework.clients.httpbin_client import HTTPBINClient


cli = HTTPBINClient()


@allure.suite('Тесты раздела "Methods"')
class TestMethods:

    @allure.title('Проверка запроса /delete с данными')
    def test_delete_with_json(self):
        with allure.step('Подготовка данных для запроса /delete'):
            json_data = {'id': 1}
        with allure.step('Отправка запроса /delete'):
            response = cli.delete_(json=json_data)
        with allure.step('Проверка ответа'):
            assert response.ok, 'response not OK'
            assert response.json()['json'] == json_data
