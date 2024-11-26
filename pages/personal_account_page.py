from pages.base_page import BasePage
from locators.main_page_locators import *
from test_personal_account_page.data import LOGIN_PKG, PASSWORD_PGK


class PersonalPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Нажимаем на кнопку "Войти"
    def login_button(self):
        self.click_element(login_button)

    # Возвращает поле логин
    def get_login_input(self):
        return self.find_element(*login_input)

    # Вводим логин
    def login_input_send_keys(self):
        self.get_login_input().send_keys(LOGIN_PKG)

    # Возвращает поле пароль
    def get_password_input(self):
        return self.find_element(*password_input)

    # Вводим логин
    def password_input_send_keys(self):
        self.get_password_input().send_keys(PASSWORD_PGK)

    # Нажимаем кнпоку "Войти"
    def click_enter_button(self):
        self.click_element(enter_button)
