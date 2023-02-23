import pytest
from app.calculator import Calculator
class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 6, 8) == 48

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 15, 5) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 18, 9) == 9

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 2, 8) == 10
