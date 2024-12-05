class TestCalculation:
    def __init__(self):
        self.quantity_case = None
        self.case_write_time = 10  # минуты на написание одного кейса
        self.case_execution_time = 10  # минуты на выполнение одного кейса
        self.defect_ratios = 5  # количество кейсов на один дефект
        self.bug_report_time = 10  # время на оформление одного баг-репорта
        self.retest_ratio = 2  # число ретестов
        self.risk_percentage = 0.3  # 30%

    def input_quantity_case(self):
        self.quantity_case = int(input("Введите количество тест-кейсов: "))

    def calculate_time_case(self):
        total_write_time = self.quantity_case * self.case_write_time
        total_execution_time = self.quantity_case * self.case_execution_time
        total_time = total_write_time + total_execution_time
        print(f"Общее время на написание и выполнение тестов: {total_time} минут")
        return total_time

    def calculate_defects(self):
        estimated_defects = self.quantity_case / self.defect_ratios
        print(f"Приблизительное количество дефектов: {int(estimated_defects)}")
        return estimated_defects

    def calculate_bug_report_time(self, estimated_defects):
        total_bug_report_time = estimated_defects * self.bug_report_time
        print(f"Время на оформление баг-репортов: {total_bug_report_time} минут")
        return total_bug_report_time

    def calculate_retest_time(self, estimated_defects):
        first_retest_time = estimated_defects * self.retest_ratio * self.bug_report_time
        print(f"Время на ретест: {first_retest_time} минут")
        return first_retest_time

    def calculate_risks(self, total_time, bug_report_time, retest_time):
        total_with_risks = (total_time + bug_report_time + retest_time) * (1 + self.risk_percentage)

        # Конвертируем минуты в часы и минуты
        hours = total_with_risks // 60
        minutes = total_with_risks % 60

        print(f"Итоговое время с рисками: {total_with_risks} минут ({int(hours)} ч {int(minutes)} мин)")
        return total_with_risks