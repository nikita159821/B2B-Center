URL = 'https://beta.b2b-center.ru/api/contract/api/documents/import'

EXPECTED_RESPONSE_BODY_MIGRATE_CHILD_DOCUMENT_PAYLOAD = {
    "user_id": 826244,
    "documents": [
        {
            "contract_external_id": "1",
            "parent_contract_external_id": "8",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-27",
            "validity_end_date": "2024-01-31",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog": "true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }
            ]
        }
    ]
}

EXPECTED_RESPONSE_BODY_MIGRATE_CHILD_DOCUMENT = {
    "status": "error",
    "errors": {
        "1": "1: Родительский документ не найден"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "1": {
                "external_id": "1",
                "data": [
                    "Родительский документ не найден"
                ]
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_DOCUMENT_ALREADY_EXISTS_PAYLOAD = {
    "user_id": 826244,
    "documents": [
        {
            "contract_external_id": "4324325435",
            "parent_contract_external_id": "",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-27",
            "validity_end_date": "2024-01-31",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog": "true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }
            ]
        }
    ]
}

EXPECTED_RESPONSE_BODY_DOCUMENT_ALREADY_EXISTS = {
    "status": "error",
    "errors": {
        "4324325435": "4324325435: Документ уже есть в системе"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "4324325435": {
                "external_id": "4324325435",
                "data": [
                    "Документ уже есть в системе"
                ]
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_SUPPLIER_NOT_FOUND_PAYLOAD = {
    "user_id": 826244,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-27",
            "validity_end_date": "2024-01-31",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "1",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_SUPPLIER_NOT_FOUND = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: Не найдена фирма поставщика по номеру делового партнёра 1"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": [
                    "Не найдена фирма поставщика по номеру делового партнёра 1"
                ]
            }
        }
    }
}


EXPECTED_RESPONSE_BODY_CONTRACT_KIND_CODE_REQUIRED_PAYLOAD = {
    "user_id": 826244,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-27",
            "validity_end_date": "2024-01-31",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_CONTRACT_KIND_CODE_REQUIRED = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: contract_kind_code - Обязательно для заполнения"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "contract_kind_code": "contract_kind_code - Обязательно для заполнения"
                }
            }
        }
    }
}


EXPECTED_RESPONSE_BODY_ITEM_NUMBER_REQUIRED_PAYLOAD = {
    "user_id": 826244,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-27",
            "validity_end_date": "2024-01-31",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_ITEM_NUMBER_REQUIRED = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: positions.0.item_number - Обязательно для заполнения; positions.1.item_number - Обязательно для заполнения"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "positions.0.item_number": "positions.0.item_number - Обязательно для заполнения",
                    "positions.1.item_number": "positions.1.item_number - Обязательно для заполнения"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_ACCOUNT_DETAILS_ID_REQUIRED_PAYLOAD = {
    "user_id": 826244,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-27",
            "validity_end_date": "2024-01-31",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_ACCOUNT_DETAILS_ID_REQUIRED = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: additional_fields_values.account_details_id - Обязательно для заполнения"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "additional_fields_values.account_details_id": "additional_fields_values.account_details_id - Обязательно для заполнения"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_INSUFFICIENT_PRIVILEGES_PAYLOAD = {
    "user_id": 828272,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-27",
            "validity_end_date": "2024-01-31",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_INSUFFICIENT_PRIVILEGES = {
    "status": "error",
    "errors": [
        "Недостаточно прав"
    ],
    "data": []
}


EXPECTED_RESPONSE_BODY_VALIDITY_START_DATE_REQUIRED_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "",
            "validity_end_date": "2024-01-31",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_VALIDITY_START_DATE_REQUIRED = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: validity_start_date - Обязательно для заполнения"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "validity_start_date": "validity_start_date - Обязательно для заполнения"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_INVALID_DATES_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "123",
            "validity_end_date": "2024-01-31",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_INVALID_DATES = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: validity_start_date - Документ не активирован - дата начала действия документа больше текущей, Не соответствует формату Y-m-d; validity_end_date - Дата окончания действия документа меньше даты начала действия"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "validity_start_date": "validity_start_date - Документ не активирован - дата начала действия документа больше текущей, Не соответствует формату Y-m-d",
                    "validity_end_date": "validity_end_date - Дата окончания действия документа меньше даты начала действия"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_INVALID_DATE_ORDER_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2023-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_INVALID_DATE_ORDER = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: validity_end_date - Дата окончания действия документа меньше даты начала действия"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "validity_end_date": "validity_end_date - Дата окончания действия документа меньше даты начала действия"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_RCM_SUM_NOT_NUMBER_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "тест",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_RCM_SUM_NOT_NUMBER = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: rcm_sum_no_nds - Здесь должно быть число"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "rcm_sum_no_nds": "rcm_sum_no_nds - Здесь должно быть число"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_RCM_SUM_INVALID_COMMA_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "23123213213212232132132132312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "1,2",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_RCM_SUM_INVALID_COMMA = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: rcm_sum_no_nds - Здесь должно быть число"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "rcm_sum_no_nds": "rcm_sum_no_nds - Здесь должно быть число"
                }
            }
        }
    }
}


EXPECTED_RESPONSE_BODY_RCM_SUM_WITH_NDS_NOT_NUMBER_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "тест",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }


EXPECTED_RESPONSE_BODY_RCM_SUM_WITH_NDS_NOT_NUMBER = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: rcm_sum_with_nds - Здесь должно быть число"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "rcm_sum_with_nds": "rcm_sum_with_nds - Здесь должно быть число"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_RCM_SUM_WITH_NDS_INVALID_COMMA_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "1,2",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog": "true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
    ]
}

EXPECTED_RESPONSE_BODY_RCM_SUM_WITH_NDS_INVALID_COMMA = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: rcm_sum_with_nds - Здесь должно быть число"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "rcm_sum_with_nds": "rcm_sum_with_nds - Здесь должно быть число"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_CONTRACT_STATE_CODE_INVALID_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "4",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_CONTRACT_STATE_CODE_INVALID = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: contract_state_code - Выбранное значение ошибочно"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "contract_state_code": "contract_state_code - Выбранное значение ошибочно"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_CONTRACT_STATE_CODE_REQUIRED_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_CONTRACT_STATE_CODE_REQUIRED = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: contract_state_code - Обязательно для заполнения"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "contract_state_code": "contract_state_code - Обязательно для заполнения"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_RCM_SIGN_PLACE_REQUIRED_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_RCM_SIGN_PLACE_REQUIRED = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: rcm_sign_place - Обязательно для заполнения"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "rcm_sign_place": "rcm_sign_place - Обязательно для заполнения"
                }
            }
        }
    }
}


EXPECTED_RESPONSE_BODY_LOAD_CATALOG_INVALID_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog": "4",  # недопустимое значение
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }
            ]
        }
    ]
}

EXPECTED_RESPONSE_BODY_LOAD_CATALOG_INVALID = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: load_catalog - Выбранное значение ошибочно"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "load_catalog": "load_catalog - Выбранное значение ошибочно"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_CURRENCY_CODE_REQUIRED_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            # Удаляем currency_code
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog": "true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001","financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }
            ]
        }
    ]
}

EXPECTED_RESPONSE_BODY_CURRENCY_CODE_NOT_FOUND_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "213213",  # недопустимое значение
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog": "true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"}
            ]
        }
    ]
}

EXPECTED_RESPONSE_BODY_PAYMENT_CONDITION_REQUIRED_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            # Удаляем payment_condition
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog": "true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }
            ]
        }
    ]
}

EXPECTED_RESPONSE_BODY_PAYMENT_CONDITION_NOT_FOUND_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "213213",  # недопустимое значение
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog": "true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001","house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }
            ]
        }
    ]
}

EXPECTED_RESPONSE_BODY_VAT_RATE_INVALID_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "тест",  # недопустимое значение
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog": "true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1000000670",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }
            ]
        }
    ]
}

EXPECTED_RESPONSE_BODY_CURRENCY_CODE_REQUIRED = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: currency_code - Обязательно для заполнения"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "currency_code": "currency_code - Обязательно для заполнения"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_CURRENCY_CODE_NOT_FOUND = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: Валюта с кодом 213213 не найдена в справочнике"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": [
                    "Валюта с кодом 213213 не найдена в справочнике"
                ]
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_PAYMENT_CONDITION_REQUIRED = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: payment_condition - Обязательно для заполнения"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "payment_condition": "payment_condition - Обязательно для заполнения"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_PAYMENT_CONDITION_NOT_FOUND = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: Условие платежа с кодом 213213 не найдено в справочнике"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": [
                    "Условие платежа с кодом 213213 не найдено в справочнике"
                ]
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_VAT_RATE_INVALID = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: vat_rate - Выбранное значение ошибочно"
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": {
                    "vat_rate": "vat_rate - Выбранное значение ошибочно"
                }
            }
        }
    }
}

EXPECTED_RESPONSE_BODY_POSITION_NOT_FOUND_PAYLOAD = {
    "user_id": 828393,
    "documents": [
        {
            "contract_external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
            "parent_contract_external_id": "0",
            "case_title": "Тра-та-та",
            "auto_renewal_category_code": "R",
            "currency_code": "RUB",
            "rcm_sum_with_nds": "12.00",
            "validity_start_date": "2023-01-13",
            "validity_end_date": "2024-01-12",
            "vat_rate": "10",
            "rcm_sign_place": "Москва, Ленина, 24",
            "payment_condition": "A500",
            "contract_kind_code": "R",
            "contract_state_code": "5",
            "payment_currency_code": "RUB",
            "rcm_sum_no_nds": "10.00",
            "business_partner_number": "123123123",
            "contract_manager": "manager@mail.ru",
            "load_catalog":"true",
            "additional_fields_values": {
                "rcm_type_summ": "N",
                "contract_category_code": "PDPD",
                "business_area_code": "1001",
                "financial_management_position": "100100000",
                "activity_category": "10100001",
                "house_bank": "ALF01",
                "account_details_id": "RP239",
                "rcm_act_period": "4",
                "business_partner_bank_record_id": "0001",
                "document_type": "S",
                "rcm_fipex": "1.2.1.0",
                "rcm_subs_id": True,
                "rcm_sub_categ": "PDPD"
            },
            "positions": [
                {
                    "item_number": "1406005",
                    "material_number": "1",
                    "unit_of_measure": "12301",
                    "quantity": "11",
                    "net_amount": "5.50",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "120"
                },
                {
                    "item_number": "1406006",
                    "material_number": "1000000670",
                    "unit_of_measure": "765",
                    "quantity": "3",
                    "net_amount": "25000",
                    "purchase_plant": "1050",
                    "warehouse": "2134",
                    "purchasing_group": "131"
                }

            ]
        }
            ]
        }

EXPECTED_RESPONSE_BODY_POSITION_NOT_FOUND = {
    "status": "error",
    "errors": {
        "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213: Позиция с кодом 1 не найдена в справочнике."
    },
    "data": {
        "imported_documents": [],
        "errors": {
            "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213": {
                "external_id": "2312321321321622321321321dasdsadsadasdsafdewjhfjksahg4321324213423432423213213",
                "data": [
                    "Позиция с кодом 1 не найдена в справочнике."
                ]
            }
        }
    }
}