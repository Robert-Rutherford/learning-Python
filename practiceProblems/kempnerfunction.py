# The Kempner Function
# site: https://edabit.com/challenge/qQnWXBsQaH73yY8r4
# The Kempner Function, applied to a composite number, permits to find the smallest integer greater than zero which
# factorial is exactly divided by the number.
#
# kempner(6) ➞ 3
#
# 1! = 1 % 6 > 0
# 2! = 2 % 6 > 0
# 3! = 6 % 6 === 0
#
# kempner(10) ➞ 5
#
# 1! = 1 % 10 > 0
# 2! = 2 % 10 > 0
# 3! = 6 % 10 > 0
# 4! = 24 % 10 > 0
# 5! = 120 % 10 === 0
# A Kempner Function applied to a prime will always return the prime itself.
#
# kempner(2) ➞ 2
# kempner(5) ➞ 5
# Given an integer n, implement a Kempner Function.


def kempner(n):
    lowest = 0
    factorial = 1
    while lowest == 0:
        fact = 1
        for x in range(1, factorial+1):
            fact = fact * x
        if (fact % n) == 0:
            return factorial
        else:
            factorial += 1


print(kempner(6))
print(kempner(10))
print(kempner(2))
