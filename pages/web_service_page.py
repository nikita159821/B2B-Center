from locators.migrated_document_page import send
from migrated_document_page.data import SEND_MIGRATION
from pages.base_page import BasePage


class MigratedDocumentPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Возвращает поле для миграции
    def get_web_service_input(self):
        return self.find_element(*send)

    # Вводим данные в поле для миграции
    def click_web_service(self):
        self.get_web_service_input().click()
        # Вводим данные в поле для миграции

    def send_web_service(self,send):
        self.get_web_service_input().send_keys()