import allure
import time

from create_application_page.data import PASSWORD_PGK
from migrated_document_page.data import LOGIN_PKG, SEND_MIGRATION
from pages.personal_account_page import PersonalPage
from pages.web_service_page import MigratedDocumentPage


class TestMigratedDocument:
    @allure.title("Валидация атрибутов для миграции")
    def test_creating_application(self, browser):
        test = MigratedDocumentPage(browser)
        test_2 = PersonalPage(browser)
        test.open_web_service()
        time.sleep(5)
        test_2.login_input_send_keys(LOGIN_PKG)
        test_2.password_input_send_keys(PASSWORD_PGK)
        test_2.click_enter_button()
        time.sleep(3)
        test.click_web_service()
        time.sleep(3)
        test.send_web_service(SEND_MIGRATION)
        time.sleep(23)
