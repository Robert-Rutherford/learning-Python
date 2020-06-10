# Count Missing Numbers
# site: https://edabit.com/challenge/vBwRuR4mF5yQ4cNuc
# Create a function that takes a list of "mostly" numbers, counts the amount of missing numbers and returns
# their sum. Watch out for strings!


def count_missing_nums(lst):
    numberlist = list()
    for element in lst:
        if element.isnumeric():
            numberlist.append(int(element))
    numberlist.sort()
    counter = 0
    checker = numberlist[0]
    index = 0
    for x in range(numberlist[0], (numberlist[len(numberlist) - 1] + 1)):
        if x == numberlist[index]:
            index += 1
        else:
            counter += 1
    return counter


print(count_missing_nums(["1", "3", "5", "7", "9"]))
print(count_missing_nums(["7", "3", "1", "9", "5"]))
print(count_missing_nums(["1", "5", "B", "9", "z"]))
