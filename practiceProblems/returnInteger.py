# Return Only the Integer
# site: https://edabit.com/challenge/DG2HLRqxFXxbaEDX4
# Write a function that takes a list of elements and returns only the integers.


def return_only_integer(lst):
    integerlist = []
    for x in lst:
        if type(x) in (float, int):
            integerlist.append(x)
    print(integerlist)


return_only_integer([9, 2, "space", "car", "lion", 16])
return_only_integer(["hello", 81, "basketball", 123, "fox"])
return_only_integer([10, "121", 56, 20, "car", 3, "lion"])
return_only_integer(["String", True, 3.3, 1])
