# Purge and Organize
# site: https://edabit.com/challenge/EZMCpHaNFg2Yfsnxx
# Given a list of numbers, write a function that returns a list that...
#
# Has all duplicate elements removed.
# Is sorted from least to greatest value.


def unique_sort(lst):
    returnlist = list()
    for x in lst:
        if x not in returnlist:
            returnlist.append(x)
    returnlist.sort()
    print(returnlist)


unique_sort([1, 2, 4, 3])
unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2])
unique_sort([6, 7, 3, 2, 1])
