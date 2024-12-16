import logging
import requests
import os
import allure
from api_b2b_center.test.data import URL

logging.basicConfig(level=logging.DEBUG)


class MigratedDocument:
    def __init__(self):
        self.response = None

    @allure.step('Отправка запроса на миграцию документа')
    def migrated_document(self, payload):
        token = os.getenv('API_TOKEN')
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        logging.debug(f"Sending request to: {URL} with headers: {headers} and payload: {payload}")
        self.response = requests.post(URL, json=payload, headers=headers)
        logging.debug(f"Response status: {self.response.status_code}")
        logging.debug(f"Response body: {self.response.text}")
        return self.response
