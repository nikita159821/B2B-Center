from pages.base_page import BasePage
from locators.requirements_page_locators import *


class RequirementsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Ищем созданную строку из заявки в РП
    def get_number_application(self):
        number_application = self.get_attribute_of_element(get_number_application, 'title')
        print(number_application)