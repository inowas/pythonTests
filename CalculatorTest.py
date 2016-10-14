import unittest
from Calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def test_SumWithTwoParameterTest(self):
        calculator = Calculator()
        self.assertEqual(5, calculator.sum(2, 3))

    def test_MultiplicationWithTwoParameterTest(self):
        calculator = Calculator()
        self.assertEqual(6, calculator.multiply(2, 3))
        self.assertEqual(6, calculator.multiply(3, 2))

    def test_MultiplicationWithOneParameterReturnSquareTest(self):
        calculator = Calculator()
        self.assertEqual(9, calculator.multiply(3))

    def test_powerof_two(self):
        calculator = Calculator()
        self.assertEqual(8, calculator.poweroftwo(3))


if __name__ == '__main__':
    unittest.main()
