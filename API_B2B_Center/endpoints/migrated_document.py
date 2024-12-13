import allure
import requests

from API_B2B_Center.test.data import URL


class MigratedDocument:
    def __init__(self):
        self.response = None

    @allure.step('Отправка запроса на миграцию документа')
    def migrated_document(self, payload):
        headers = {
            'Authorization': 'Bearer aa75f047af75a1a7337444d5fe27bd91',
            'Content-Type': 'application/json'
        }

        self.response = requests.post(URL, json=payload, headers=headers)
        return self.response


