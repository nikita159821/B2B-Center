import time

from pages.base_page import BasePage


class Test:
    def test_2(self,browser):
        test = BasePage(browser)
        test.open_catalog()
        time.sleep(30)