import time

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
    expected: int = 3

    # Act
    actual: int = calculator.divide(a, b)

    # Assert
    assert expected == actual, "small numbers divide"
# pip install pytest
# option 1- run the tests : play
# option 2- run the tests
#         in the Terminal : pytest .
# add test sub
# add test mul
# add test div