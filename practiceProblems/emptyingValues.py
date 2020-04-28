# Emptying the values
# site: https://edabit.com/challenge/zNNtsPBCE5FFXW7wn
# Given a list of values, return a list with each value replaced with the empty value of the same type. More explicitly:
#
# replace integers (e.g. 1, 3), whose type is "int", with 0
# replace floats (e.g. 3.14, 2.17), whose type is "float", with 0.0
# replace strings (e.g. 'abcde', 'x'), whose type is "str", with ''
# replace booleans (True, False), whose type is "bool", with False
# replace lists (e.g. [1, 'a', 5], [[4]]), whose type is "list", with []
# replace tuples (e.g. (1,9,0), (2,)), whose type is "tuple", with ()
# replace sets (e.g. {0,'a'}, {'b'}), whose type is "set", with set() (caution: python interprets {} as the empty
# dictionary, not the empty set)
# None, whose type is "NoneType", is preserved as None


def empty_values(lst):
    returnlist = list()
    for x in lst:
        if isinstance(x, bool):
            returnlist.append(False)
        elif isinstance(x, int):
            returnlist.append(0)
        elif isinstance(x, float):
            returnlist.append(0.0)
        elif isinstance(x, str):
            returnlist.append('')
        elif isinstance(x, list):
            returnlist.append(list())
        elif isinstance(x, tuple):
            returnlist.append(tuple())
        elif isinstance(x, set):
            returnlist.append(set())
        else:
            returnlist.append(None)
    return returnlist


print(empty_values([1, 2, 3]))
print(empty_values([7, 3.14, 'cat']))
print(empty_values([[1, 2, 3], (1, 2, 3), {1, 2, 3}]))
print(empty_values([[7, 3.14, 'cat']]))
print(empty_values([None]))
