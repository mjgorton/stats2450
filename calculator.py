#Exercise 2

def calculate(num1, num2):
    """
    a calculator
    """
    total = num1 +num2
    diff = num1 - num2
    prod = num1 * num2
    quot = num1 / num2

    return total, diff, prod, quot

print(calculate(10, 3))

total, diff, prod, quot = calculate(10, 0)

