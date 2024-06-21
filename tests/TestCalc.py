import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_adding(self):
        assert self.calc.adding(self,1, 1) == 2

    def test_adding_subtraction(self):
        assert self.calc.subtraction(self,5, 2) == 3

    def test_adding_multiply(self):
        assert self.calc.multiply(self,2, 2) == 4

    def test_zero_division(self):
        assert self.calc.division(self,2, 1) == 2

    def teardown(self):
        print('Выполнение метода Teardown')