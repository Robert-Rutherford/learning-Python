# Flip the Array
# site: https://edabit.com/challenge/QoavwQhmrDpXJhBW9
# Create a function that flips a horizontal list into a vertical list, and a vertical list into a horizontal list.
#
# In other words, take an 1 x n list (1 row + n columns) and flip it into a n x 1 list (n rows and 1 column), and
# vice versa.


def flip_list(lst):
    vertical = len(lst)
    horizontal = 0
    allvalues = list()
    newlst = list()
    index = 0
    if vertical == 0:
        return newlst
    for item in lst:
        if type(item) is list:
            itemlength = len(item)
            if itemlength > horizontal:
                horizontal = len(item)
        else:
            horizontal = 1
    for items in lst:
        if type(items) is list:
            for value in items:
                allvalues.append(value)
        else:
            allvalues.append(items)
    for x in range(vertical):
        row = list()
        for y in range(horizontal):
            row.append(allvalues[index])
            index += 1
        newlst.append(row)
    return newlst


print(flip_list([1, 2, 3, 4]))
print(flip_list([[5], [6], [9]]))
print(flip_list([]))

