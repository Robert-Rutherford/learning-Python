# Junction or Self?
# site: https://edabit.com/challenge/72XK73LFkd7wuakwZ
# In this challenge, you have to separate integers into two families, establishing if they are Junction Numbers or
# Self Numbers. Given a number n:
#
# If exists at least a single number which added to the sum of its digits is equal to n, then n is a Junction Number.
#
# If there are not numbers which added to the sum of their digits are equal to n, then n is a Self Number.
#
# Given a positive integer n, implement a function that returns:
#
# The string "Self" if n is a Self Number.
# If n is a Junction Number an array, ordered descendingly, containing the numbers which generate n.


def junction_or_self(n):
    junction = list()
    for x in range(1, n):
        number = str(x)
        num = x
        for index in range(len(number)):
            num += int(number[index])
        if num == n:
            junction.append(x)
    if len(junction) >= 1:
        return junction
    else:
        return "Self"


print(junction_or_self(25))
print(junction_or_self(818))
print(junction_or_self(7))
