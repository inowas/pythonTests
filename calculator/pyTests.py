from Calculator import Calculator


def test_sum_with_integers():
    calculator = Calculator()
    assert calculator.sum(3, 2) == 5


def test_sum_with_two_valid_strings():
    calculator = Calculator()
    assert calculator.sum("5", "10") == 15


def test_sum_with_one_valid_string():
    calculator = Calculator()
    assert calculator.sum("5", 20) == 15



