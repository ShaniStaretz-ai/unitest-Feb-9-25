import math


def add(a, b):
    return a + b  # + 0.1 # 0.99999999999


# 0.4444444444 + 0.66666666666
# 0.999999999999
# 1.0

def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

def say_hello():
    name = input("enter name? ")
    return f"hello {name}"

#########################################################
#homework

def power(a: int, b: int) -> int:
    return a ** b;


def sqrt(a: int) -> float:
    return math.sqrt(a);


def factorial(a) -> int:
    result = 1
    if a < 0:
        raise ValueError();
    if a==0:
        return 1
    for i in range(1, a + 1):
        result *= i
    return result
