# Combined Consecutive Sequence
# site: https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb
# Write a function that returns True if two lists, when combined, form a consecutive sequence.


def consecutive_combo(lst1, lst2):
    combinedlist = lst1 + lst2
    combinedlist.sort()
    count = int(combinedlist[0])
    for num in combinedlist:
        if num != count:
            return False
        count = count + 1
    return True


print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
print(consecutive_combo([44, 46], [45]))
