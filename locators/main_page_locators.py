from selenium.webdriver.common.by import By


login_button = (By.XPATH, '//button[@class="cds-theme--cds cds-button__appearance--transparent cds-button__size--sm cds-button--invert-color cds-button core-header-auth__button"]')
login_input = (By.ID, 'login_control')
password_input = (By.ID, 'password_control')
enter_button = (By.ID, 'enter_button')
lk_button = (By.XPATH, '//div[@class="header-account gt-lg"]')
button_products_and_services = (By.XPATH, '//a[@aria-controls="/catalog/personal/"]')
button_create_request = (By.ID, 'create_regular_procedure_request_button')
button_list_positions = (By.XPATH, '//*[@id="page"]/main/div/div/nav/div/div[2]/div/div/div[2]/ul/li[2]/a')
button_upload_file = (By.XPATH, '//*[@id="page"]/main/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/button[2]')
button_send_approval = (By.XPATH, '//form[@class="cds-form"]/button[2]')
button_send = (By.XPATH, '//section[@class="cds-modal cds-modal--md"]/footer[@class="cds-modal__footer"]/button[2]')
button_output_lk = (By.XPATH, '//a[@class="hidden-mobile"]')
button_approval = (By.XPATH,'//*[@id="page"]/main/div/div/nav/div/div[1]/div/div[2]/div/form/button[2]')
button_approval_form = (By.XPATH,'//*[@id="lfms"]/section/footer/button[2]')