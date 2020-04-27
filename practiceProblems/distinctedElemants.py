# Two Distinct Elements
# site: https://edabit.com/challenge/yL5WmWTCNwwb4GnR7
# In each input list, every number repeats at least once, except for two.
#
# Write a function that returns the two unique numbers.


def return_unique(lst):
    cleanedlist = list()
    uniquelist = list()
    for num in lst:
        if num not in cleanedlist:
            cleanedlist.append(num)
            uniquelist.append(num)
        else:
            if num in uniquelist:
                uniquelist.remove(num)
    return uniquelist


print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))
