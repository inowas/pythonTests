import unittest
from Calculator import Calculator


class SumTest(unittest.TestCase):
    def test(self):
        calculator = Calculator()
        self.assertEqual(5, calculator.sum(2, 3))
