import time
from pages.personal_account_page import PersonalPage


class Test:
    def test_2(self, browser):
        test = PersonalPage(browser)
        test.open_catalog()
        time.sleep(5)
        test.login_button()
        time.sleep(2)
        test.login_input_send_keys()
        time.sleep(2)
        test.password_input_send_keys()
        time.sleep(5)
        test.click_enter_button()
        time.sleep(30)
