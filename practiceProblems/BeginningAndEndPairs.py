# Beginning and End Pairs
# site: https://edabit.com/challenge/HrCuzAKE6skEYgDmf
# Write a function that pairs the first number in an array with the last, the second number with the second to last,
# etc.
# notes:
# If the list has an odd length, repeat the middle element twice for the last pair.
# Return an empty list if the input is an empty list.


def pairs(lst):
    pairedlist = list()
    split = 0
    reverse = -1
    odd = False
    if len(lst) % 2 == 0:
        split = int(len(lst)/2)
    else:
        odd = True
        split = int(int(len(lst))/2)
    for x in range(split):
        pairset = list()
        pairset.append(lst[x])
        pairset.append(lst[reverse])
        reverse -= 1
        pairedlist.append(pairset)
    if odd:
        oddset = list()
        oddset.append(lst[split])
        oddset.append(lst[split])
        pairedlist.append(oddset)
    return pairedlist


print(pairs([1, 2, 3, 4, 5, 6, 7]))
print(pairs([1, 2, 3, 4, 5, 6]))
print(pairs([5, 9, 8, 1, 2]))
print(pairs([]))
