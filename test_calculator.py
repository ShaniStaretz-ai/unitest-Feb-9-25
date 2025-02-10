import pytest

import calculator


def test_calculator_add_small():
    # Arrange
    a: int = 2
    b: int = 5
    expected: int = 7

    # Act
    actual: int = calculator.add(a, b)

    # Assert
    assert expected == actual, "small numbers add"


def test_calculator_minus_small():
    # Arrange
    a: int = 5
    b: int = 2
    expected: int = 3

    # Act
    actual: int = calculator.minus(a, b)

    # Assert
    assert expected == actual, "small numbers minus"


def test_calculator_multiply_small():
    # Arrange
    a: int = 2
    b: int = 5
    expected: int = 10

    # Act
    actual: int = calculator.multiply(a, b)

    # Assert
    assert expected == actual, "small numbers multiply"


def test_calculator_divide_small():
    # Arrange
    a: int = 10
    b: int = 5
    expected: int = 2

    # Act
    actual: int = calculator.divide(a, b)

    # Assert
    assert expected == actual, "small numbers divide"


def test_calculator_hello(monkeypatch):
    # black box
    monkeypatch.setattr('builtins.input', lambda _: "danny")

    expected = "hello danny"
    result = calculator.say_hello()

    assert expected == result


########################################################

@pytest.mark.parametrize("a,b,expected", [(2, 4, 16), (3, 2, 9)])  # Arrange
def test_calculator_power_small(a, b, expected):
    # Act
    actual: int = calculator.power(a, b)

    # Assert
    assert expected == actual, f"sent {a},{b} ,expected {expected} :power small numbers"


@pytest.mark.parametrize("a,expected", [(25, 5)])  # Arrange
def test_calculator_sqrt_small_positive(a, expected):
    # Act
    actual: float = calculator.sqrt(a)

    # Assert
    assert expected == actual, f"sent {a},expected {expected} : sqrt small positive numbers  "


def test_calculator_sqrt_small_negative():
    # Arrange
    a: int = -5
    # Act
    with pytest.raises(ValueError) as ex:
        actual: float = calculator.sqrt(a)


@pytest.mark.parametrize("a,expected", [(4, 24), (5, 120),(0,1)])
def test_calculator_factorial_small_positive_numbers(a, expected):
    # Act
    actual: float = calculator.factorial(a)
    assert expected == actual, f"sent {a},expected {expected} : factorial small positive numbers  "


def test_calculator_factorial_small_negative_numbers():
    # Arrange
    a: int = -3
    # Act
    with pytest.raises(ValueError) as ex:
        actual: float = calculator.factorial(a)

