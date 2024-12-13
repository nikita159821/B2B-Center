from estimation.calculate import TestCalculation


def main():
    calc = TestCalculation()
    calc.input_quantity_case()  # Запрос количества тест-кейсов
    total_time = calc.calculate_time_case()  # Общие затраты времени на тесты
    estimated_defects = calc.calculate_defects()  # Количество дефектов
    bug_report_time = calc.calculate_bug_report_time(estimated_defects)  # Время на баг-репорты
    retest_time = calc.calculate_retest_time(estimated_defects)  # Время на ретесты
    calc.calculate_risks(total_time, bug_report_time, retest_time)  # Итоговое время с учетом рисков


if __name__ == "__main__":
    main()
