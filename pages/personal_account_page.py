import time
import pyperclip
from create_application_page.urls import BETA_URL
from pages.base_page import BasePage
import pyautogui
from locators.main_page_locators import *


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
    def login_input_send_keys(self, login):
        self.get_login_input().send_keys(login)

    # Вводим пароль
    def password_input_send_keys(self, password):
        self.get_password_input().send_keys(password)

    # Нажимаем кнпоку "Войти"
    def click_enter_button(self):
        self.click_element(enter_button)

    # Объединённый метод для входа в ЛК
    def login(self, login, password):
        self.login_input_send_keys(login)
        self.password_input_send_keys(password)
        self.click_enter_button()

    # Возвращает поле пароль
    def get_password_input(self):
        return self.find_element(*password_input)

    # Нажимаем кнопку "Личный кабинет"
    def click_lk_button(self):
        self.click_element(lk_button)

    # Нажимаем кнопку "Товары и услуги". Пока не используем, так как не работает переход по кнопке
    def click_button_products_and_services(self):
        self.click_element(button_products_and_services)

    # Нажимаем кнопку "Создать заявку"
    def click_button_create_request(self):
        self.click_element(button_create_request)

    # Нажимаем кнопку "Список позиций"
    def click_button_list_positions(self):
        self.click_element(button_list_positions)

    # Нажимаем кнопку "Загрузить из файла"
    def click_button_upload_file(self):
        self.click_element(button_upload_file)

    # Загружаем файл с позицией
    @staticmethod
    def get_button_upload_file():
        time.sleep(5)  # Дождитесь, пока окно загрузки активируется
        file_path = r"C:\Users\user\Downloads\1.2.xlsx"

        # Копируем путь в буфер обмена
        test = pyperclip.copy(file_path)
        print(test)

        # Вставляем путь
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Задержка перед нажатием Enter
        pyautogui.press('enter')

    # Нажимаем кнопку "Отправить на согласование"
    def click_button_send_approval(self):
        self.click_element(button_send_approval)

    # Нажимаем кнопку "Отправить"
    def click_button_send(self):
        self.click_element(button_send)

    # Сохраняем url страницы с заявкой
    def save_url_application(self):
        return self.get_current_url()

    # Выходим из лк
    def click_button_output_lk(self):
        self.click_element(button_output_lk)

    # Нажимаем кнопку "Согласовать"
    def click_button_approval(self):
        self.click_element(button_approval)

    # Нажимаем кнопку "Согласовать" в форме подтверждения
    def click_button_approval_form(self):
        self.click_element(button_approval_form)

    # Объединённый метод для выполнения действий
    def perform_action(self):
        self.click_button_approval()
        time.sleep(4)
        self.click_button_approval_form()
        time.sleep(4)
        self.click_button_output_lk()
        time.sleep(4)

    # Открывает раздел "Товары и услуги"
    def open_products_and_services(self):
        self.browser.get(f'{BETA_URL}')

    # Объединённый метод для открытия раздела и создания заявки
    def open_products_and_services_and_create_request(self):
        self.browser.get(f'{BETA_URL}')  # Открываем раздел "Товары и услуги"
        time.sleep(5)
        self.click_element(button_create_request)  # Нажимаем кнопку "Создать заявку"
        time.sleep(10)
        self.click_element(button_list_positions)  # Нажимаем кнопку "Список позиций"
        time.sleep(2)
        self.click_element(button_upload_file)  # Нажимаем кнопку "Загрузить из файла"
        time.sleep(2)
        self.get_button_upload_file()
        time.sleep(2)  # Загружаем файл с позицией
        self.click_button_send_approval()  # Нажимаем кнопку "Отправить на согласование"
        time.sleep(5)
        self.click_button_send()  # Нажимаем кнопку "Отправить"
        time.sleep(7)
