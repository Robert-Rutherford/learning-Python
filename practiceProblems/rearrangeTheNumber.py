# Rearrange the Number
# site: https://edabit.com/challenge/jwzAdBnJnBxCe4AXP
# Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits
# are rearranged.


def rearranged_difference(num):
    listnum = list()
    for x in str(num):
        listnum.append(x)
    listnum.sort()
    joiner = ""
    smallest = int(joiner.join(listnum))
    listnum.reverse()
    largest = int(joiner.join(listnum))
    return largest - smallest


print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))
