# Hole Number Sequence
# site: https://edabit.com/challenge/2tkcbQgPJZPPpzg2i
# What do the digits 0, 4, 6, 8, and 9 have in common? Well, they are whole numbers... and they are also hole numbers
# (not actually a thing until now). Hole numbers are numbers with holes in their shapes (8 is special in that it
# contains two holes).
#
# 14 is a hole number with one hole. 88 is a hole number with four holes.
#
# Your task is to create a function with argument N that returns the sum of the holes for the integers n in the range
# of range 0 < n <= N.
#
# To illustrate, sum_of_holes(14) returns 7, because there are 7 holes in 4, 6, 8, 9, 10 and 14.


def sum_of_holes(N):
    count = 0
    for x in range(1, N+1):
        number = str(x)
        for num in number:
            if num == "0" or num == "4" or num == "6" or num == "9":
                count += 1
            elif num == "8":
                count += 2
    return count


print(sum_of_holes(4))
print(sum_of_holes(6))
print(sum_of_holes(8))
print(sum_of_holes(6259))
