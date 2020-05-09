# Power Ranger
# site: https://edabit.com/challenge/abdsaD6gwjgAgevsG
# Create a function that takes in n, a, b and returns the number of values raised to the nth power that lie
# in the range [a, b], inclusive.


def power_ranger(power, minimum, maximum):
    n = 1
    count = 0
    while pow(n, power) <= maximum:
        if minimum <= pow(n, power) <= maximum:
            count += 1
        n += 1
    return count


print(power_ranger(2, 49, 65))
print(power_ranger(3, 1, 27))
print(power_ranger(10, 1, 5))
print(power_ranger(5, 31, 33))
print(power_ranger(4, 250, 1300))
