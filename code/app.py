from logic.calculations import Calculation

class Math:
    def __init__(self):
        self.cal = Calculation()

    def add(self, num1, num2):
        val=self.cal.perform_add(num1, num2)
        val=self.cal.perform_add(num1, num2)
        return val

    def sub(self, num1, num2):
        return self.cal.perform_sub(num1, num2)

    def multiple(self, num1, num2):
        return self.cal.perform_nul(num1, num2)

    def divide(self, num1, num2):
        return self.cal.perform_div(num1, num2)

