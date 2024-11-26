from selenium.webdriver.common.by import By


login_button = (By.XPATH, '//button[@class="cds-theme--cds cds-button__appearance--transparent cds-button__size--sm cds-button--invert-color cds-button core-header-auth__button"]')
login_input = (By.ID, 'login_control')
password_input = (By.ID, 'password_control')
enter_button = (By.ID, 'enter_button')