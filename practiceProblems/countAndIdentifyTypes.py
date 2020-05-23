# Count and Identify Data Types
# site: https://edabit.com/challenge/HXkpnCxJgxkFwaReT
# Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.
#
# List order is:
#
# [int, str, bool, list, tuple, dictionary]


def count_datatypes(*args):
    typecount = [0, 0, 0, 0, 0, 0]
    for arg in args:
        argtype = type(arg)
        if argtype is int:
            typecount[0] += 1
        elif argtype is str:
            typecount[1] += 1
        elif argtype is bool:
            typecount[2] += 1
        elif argtype is list:
            typecount[3] += 1
        elif argtype is tuple:
            typecount[4] += 1
        elif argtype is dict:
            typecount[5] += 1
    return typecount


print(count_datatypes(1, 45, "Hi", False))
print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1))
print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23))
print(count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]))
