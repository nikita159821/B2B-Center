import allure

from API_B2B_Center.endpoints.migrated_document import MigratedDocument
from API_B2B_Center.test.data import EXPECTED_RESPONSE_BODY_MIGRATE_CHILD_DOCUMENT, \
    EXPECTED_RESPONSE_BODY_DOCUMENT_ALREADY_EXISTS, EXPECTED_RESPONSE_BODY_DOCUMENT_ALREADY_EXISTS_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_MIGRATE_CHILD_DOCUMENT_PAYLOAD, EXPECTED_RESPONSE_BODY_SUPPLIER_NOT_FOUND_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_SUPPLIER_NOT_FOUND, EXPECTED_RESPONSE_BODY_CONTRACT_KIND_CODE_REQUIRED_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_CONTRACT_KIND_CODE_REQUIRED, EXPECTED_RESPONSE_BODY_ITEM_NUMBER_REQUIRED_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_ITEM_NUMBER_REQUIRED, EXPECTED_RESPONSE_BODY_ACCOUNT_DETAILS_ID_REQUIRED_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_ACCOUNT_DETAILS_ID_REQUIRED, EXPECTED_RESPONSE_BODY_INSUFFICIENT_PRIVILEGES_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_INSUFFICIENT_PRIVILEGES, EXPECTED_RESPONSE_BODY_VALIDITY_START_DATE_REQUIRED_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_VALIDITY_START_DATE_REQUIRED, EXPECTED_RESPONSE_BODY_INVALID_DATES_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_INVALID_DATES, EXPECTED_RESPONSE_BODY_INVALID_DATE_ORDER_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_INVALID_DATE_ORDER, EXPECTED_RESPONSE_BODY_RCM_SUM_NOT_NUMBER_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_RCM_SUM_NOT_NUMBER, EXPECTED_RESPONSE_BODY_RCM_SUM_INVALID_COMMA_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_RCM_SUM_INVALID_COMMA, EXPECTED_RESPONSE_BODY_RCM_SUM_WITH_NDS_NOT_NUMBER_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_RCM_SUM_WITH_NDS_NOT_NUMBER, EXPECTED_RESPONSE_BODY_RCM_SUM_WITH_NDS_INVALID_COMMA_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_RCM_SUM_WITH_NDS_INVALID_COMMA, EXPECTED_RESPONSE_BODY_CONTRACT_STATE_CODE_INVALID_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_CONTRACT_STATE_CODE_INVALID, EXPECTED_RESPONSE_BODY_CONTRACT_STATE_CODE_REQUIRED_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_CONTRACT_STATE_CODE_REQUIRED, EXPECTED_RESPONSE_BODY_RCM_SIGN_PLACE_REQUIRED_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_RCM_SIGN_PLACE_REQUIRED, EXPECTED_RESPONSE_BODY_LOAD_CATALOG_INVALID, \
    EXPECTED_RESPONSE_BODY_LOAD_CATALOG_INVALID_PAYLOAD, EXPECTED_RESPONSE_BODY_CURRENCY_CODE_REQUIRED_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_CURRENCY_CODE_REQUIRED, EXPECTED_RESPONSE_BODY_CURRENCY_CODE_NOT_FOUND_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_CURRENCY_CODE_NOT_FOUND, EXPECTED_RESPONSE_BODY_PAYMENT_CONDITION_REQUIRED_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_PAYMENT_CONDITION_REQUIRED, EXPECTED_RESPONSE_BODY_PAYMENT_CONDITION_NOT_FOUND_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_PAYMENT_CONDITION_NOT_FOUND, EXPECTED_RESPONSE_BODY_VAT_RATE_INVALID_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_VAT_RATE_INVALID, EXPECTED_RESPONSE_BODY_POSITION_NOT_FOUND_PAYLOAD, \
    EXPECTED_RESPONSE_BODY_POSITION_NOT_FOUND


class TestMigratedDocument:
    @allure.title('Миграция дочернего документа без привязки к родительскому')
    def test_migrate_child_document_without_parent_link(self):
        migrate_child_document = MigratedDocument()
        response = migrate_child_document.migrated_document(EXPECTED_RESPONSE_BODY_MIGRATE_CHILD_DOCUMENT_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_MIGRATE_CHILD_DOCUMENT

    @allure.title('Миграция существующего документа')
    def test_migrate_existing_document(self):
        migrate_existing_document = MigratedDocument()
        response = migrate_existing_document.migrated_document(EXPECTED_RESPONSE_BODY_DOCUMENT_ALREADY_EXISTS_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_DOCUMENT_ALREADY_EXISTS

    @allure.title('Миграция документа с несуществующим поставщиком')
    def test_migrate_supplier_not_found(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_SUPPLIER_NOT_FOUND_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_SUPPLIER_NOT_FOUND

    @allure.title('Миграция документа без contract_kind_code')
    def test_migrate_missing_contract_kind_code(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_CONTRACT_KIND_CODE_REQUIRED_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_CONTRACT_KIND_CODE_REQUIRED

    @allure.title('Миграция документа без item_number')
    def test_migrate_missing_item_number_positions(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_ITEM_NUMBER_REQUIRED_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_ITEM_NUMBER_REQUIRED

    @allure.title('Миграция документа без account_details_id')
    def test_migrate_missing_account_details_id(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_ACCOUNT_DETAILS_ID_REQUIRED_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_ACCOUNT_DETAILS_ID_REQUIRED

    @allure.title('Миграция документа с недостаточными правами')
    def test_migrate_insufficient_privileges(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_INSUFFICIENT_PRIVILEGES_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 403
        assert response_body == EXPECTED_RESPONSE_BODY_INSUFFICIENT_PRIVILEGES

    @allure.title('Миграция документа без validity_start_date')
    def test_create_parent_document_missing_validity_start_date(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_VALIDITY_START_DATE_REQUIRED_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_VALIDITY_START_DATE_REQUIRED

    @allure.title('Миграция документа с некорректной validity_start_date и validity_end_date')
    def test_create_parent_document_invalid_dates(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_INVALID_DATES_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_INVALID_DATES

    @allure.title('Миграция документа с validity_end_date меньше validity_start_date')
    def test_create_parent_document_invalid_date_order(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_INVALID_DATE_ORDER_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_INVALID_DATE_ORDER

    @allure.title('Миграция документа с строковым значением rcm_sum_no_nds')
    def test_create_parent_document_invalid_rcm_sum(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_RCM_SUM_NOT_NUMBER_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_RCM_SUM_NOT_NUMBER

    @allure.title('Миграция документа с запятой в теге rcm_sum_no_nds')
    def test_create_parent_document_invalid_rcm_sum_with_comma(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_RCM_SUM_INVALID_COMMA_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_RCM_SUM_INVALID_COMMA

    @allure.title('Миграция документа с строковым значением rcm_sum_with_nds')
    def test_create_parent_document_invalid_rcm_sum_with_text(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_RCM_SUM_WITH_NDS_NOT_NUMBER_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_RCM_SUM_WITH_NDS_NOT_NUMBER

    @allure.title('Миграция документа с запятой в теге rcm_sum_with_nds')
    def test_create_parent_document_invalid_rcm_sum_with_comma(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_RCM_SUM_WITH_NDS_INVALID_COMMA_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_RCM_SUM_WITH_NDS_INVALID_COMMA

    @allure.title('Миграция документа с значением 4 в теге contract_state_code')
    def test_create_parent_document_invalid_contract_state_code(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_CONTRACT_STATE_CODE_INVALID_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_CONTRACT_STATE_CODE_INVALID

    @allure.title('Миграция документа с пустым тегом contract_state_code')
    def test_create_parent_document_missing_contract_state_code(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_CONTRACT_STATE_CODE_REQUIRED_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_CONTRACT_STATE_CODE_REQUIRED

    @allure.title('Миграция документа с пустым тегом rcm_sign_place')
    def test_create_parent_document_missing_contract_state_code(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_RCM_SIGN_PLACE_REQUIRED_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_RCM_SIGN_PLACE_REQUIRED

    @allure.title('Создание родительского документа с недопустимым значением load_catalog')
    def test_create_parent_document_invalid_load_catalog(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_LOAD_CATALOG_INVALID_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_LOAD_CATALOG_INVALID

    @allure.title('Создание родительского документа с пустым значением currency_code')
    def test_create_parent_document_missing_currency_code(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_CURRENCY_CODE_REQUIRED_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_CURRENCY_CODE_REQUIRED

    @allure.title('Создание родительского документа с несущ.значением currency_code')
    def test_create_parent_document_invalid_currency_code(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_CURRENCY_CODE_NOT_FOUND_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_CURRENCY_CODE_NOT_FOUND

    @allure.title('Создание родительского документа с пустым значением payment_condition')
    def test_create_parent_document_missing_payment_condition(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_PAYMENT_CONDITION_REQUIRED_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_PAYMENT_CONDITION_REQUIRED

    @allure.title('Создание родительского документа с несущ.значением payment_condition')
    def test_create_parent_document_invalid_payment_condition(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_PAYMENT_CONDITION_NOT_FOUND_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_PAYMENT_CONDITION_NOT_FOUND

    @allure.title('Создание родительского документа со строкой в теге vat_rate')
    def test_create_parent_document_invalid_vat_rate(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_VAT_RATE_INVALID_PAYLOAD)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_VAT_RATE_INVALID

    @allure.title('Создание родительского документа с несущ.значением material_number')
    def test_create_parent_document_invalid_material_number(self):
        migrate_document = MigratedDocument()
        response = migrate_document.migrated_document(EXPECTED_RESPONSE_BODY_POSITION_NOT_FOUND_PAYLOAD)  # Передаем переменную
        response_body = response.json()

        assert response.status_code == 200
        assert response_body == EXPECTED_RESPONSE_BODY_POSITION_NOT_FOUND