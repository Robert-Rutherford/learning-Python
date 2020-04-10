# Intro to Nested Loops
# site: https://edabit.com/challenge/YnsBcniRG9k77SSvA
# Imagine a school that kids attend for 6 years. In each year, there are five groups started, marked with the letters
# a, b, c, d, e. For the first year, the groups are 1a, 1b, 1c, 1d, 1e and for the last year, the groups
# are 6a, 6b, 6c, 6d, 6e.
#
# Write a function that returns the groups in the school by year (as a string), separated with a comma and a space
# in the form of "1a, 1b, 1c, 1d, 1e, 2a, 2b (....) 5d, 5e, 6a, 6b, 6c, 6d, 6e".


def print_all_groups():
    letters = ["a", "b", "c", "d", "e"]
    printstring = ""
    for x in range(1, 7):
        for letter in letters:
            printstring = printstring + str(x) + letter + ", "
    print(printstring)


print_all_groups()
