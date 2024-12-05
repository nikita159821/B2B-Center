import time
import allure
from pages.personal_account_page import PersonalPage
from pages.requirements_page import RequirementsPage
from create_application_page.data import LOGIN_PKG, PASSWORD_PGK, LOGIN_PKG_COORDINAT, PASSWORD_PGK_COORDINAT, \
    LOGIN_PKG_COORDINAT_2, PASSWORD_PGK_COORDINAT_2


class TestCreatingApplication:
    @allure.title("Создание заявки с согласованием, сценарий 1.2")
    def test_creating_application(self, browser):
        personal = PersonalPage(browser)
        requirements = RequirementsPage(browser)
        personal.open_catalog()
        time.sleep(5)
        personal.login_button()
        time.sleep(2)
        personal.login(LOGIN_PKG, PASSWORD_PGK)
        time.sleep(2)
        personal.open_products_and_services_and_create_request()
        url_application = personal.save_url_application()
        application = url_application.split('/')[-2].strip('/')
        personal.click_button_output_lk()
        time.sleep(10)
        personal.login(LOGIN_PKG_COORDINAT, PASSWORD_PGK_COORDINAT)
        time.sleep(3)
        personal.open(url_application)
        time.sleep(7)
        personal.perform_action()
        time.sleep(5)
        personal.login(LOGIN_PKG_COORDINAT_2, PASSWORD_PGK_COORDINAT_2)
        time.sleep(3)
        personal.open(url_application)
        time.sleep(5)
        personal.perform_action()
        time.sleep(5)
        personal.login(LOGIN_PKG, PASSWORD_PGK)
        time.sleep(2)
        personal.open_personal_requirements()
        time.sleep(10)
        numbers = requirements.get_number_application()
        time.sleep(10)
        if application == numbers:
            print(numbers)
        else:
            print('Не прокатило не фартануло')
