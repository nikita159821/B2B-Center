from selenium.webdriver.common.by import By


class LoginButton:
    login_button = (By.XPATH, '//div[@class="header-main-right"]/a[@id="auth_ajax_modal_trigger"]')