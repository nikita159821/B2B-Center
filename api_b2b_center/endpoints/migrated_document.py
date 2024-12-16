import os
import requests
from dotenv import load_dotenv
import allure
from api_b2b_center.test.data import URL

# Загрузка переменных окружения из .env файла
load_dotenv()

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

        self.response = requests.post(URL, json=payload, headers=headers)
        return self.response


