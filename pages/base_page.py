from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from create_application_page.urls import URL, BETA_URL, CATALOG, REGISTR, REQUIREMENTS


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
        self.browser.get(f'{URL}{REGISTR}')


    # Открывает страницу с РП
    def open_personal_requirements(self):
        self.browser.get(f'{URL}{REQUIREMENTS}')

    # Возвращаем текущую страницу
    def get_current_url(self):
        return self.browser.current_url

    # Открываем страницу
    def open(self, url):
        self.browser.get(url)

    # Общий метод для получения атрибута элемента
    def get_attribute_of_element(self, locator, attribute):
        element = self.find(locator)
        return element.get_attribute(attribute)