from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_personal_account_page.urls import URL
class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(self.browser)

    def wait(self, locator):
        WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.browser.find_element(*locator)

    def find_element(self, *args):
        return self.browser.find_element(*args)

    def find_elements(self, *args):
        return self.browser.find_elements(*args)

    # Общий метод для поиска элемента
    def find(self, locator):
        return self.find_element(*locator)

    # Общий метод для клика по элементу
    def click_element(self, locator):
        element = self.find(locator)
        element.click()

    # Открываем страницу каталога
    def open_catalog(self):
        self.browser.get(f'{URL}')