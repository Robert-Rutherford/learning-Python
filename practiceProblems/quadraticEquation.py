# Quadratic Equation
# site: https://edabit.com/challenge/MDWFcHCTiJfHmwTFx
# Create a function to find only the root value of x in any quadratic equation ax^2 + bx + c. The function
# will take three arguments:
#
# a as the coefficient of x^2
# b as the coefficient of x
# c as the constant term
import math


def quadratic_equation(a, b, c):
    x = (0 - b + math.sqrt((b ** 2) - (4 * a * c)))/(2 * a)
    return x


print(quadratic_equation(1, 2, -3))
print(quadratic_equation(2, -7, 3))
print(quadratic_equation(1, -12, -28))
