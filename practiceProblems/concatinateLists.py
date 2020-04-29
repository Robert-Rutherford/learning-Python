# Concatenate Variable Number of Input Lists
# site: https://edabit.com/challenge/woA74HtrheoQva87R
# Create a function that concatenates n input lists, where n is variable.


def concat(*args):
    outlist = list()
    for arg in args:
        if isinstance(arg, list):
            for ele in arg:
                outlist.append(ele)
    return outlist


print(concat([1, 2, 3], [4, 5], [6, 7]))
print(concat([1], [2], [3], [4], [5], [6], [7]))
print(concat([1, 2], [3, 4]))
print(concat([4, 4, 4, 4, 4]))
