# Drunken Python
# site: https://edabit.com/challenge/pfn6QRn6eiTHEPpSs
# Python got drunk and the built-in functions str() and int() are acting odd.
#
# Examples of drunken Python odd behavior
# str(4) ➞ 4
#
# str('4') ➞ 4
#
# int('4') ➞ '4'
#
# int(4) ➞ '4'
# You need to create two functions to substitute str() and int(). A function called int_to_str() that converts
# integers into strings and a function called str_to_int() that converts strings into integers


def int_to_str(num):
    if isinstance(num, int):
        return f"{num}"
    else:
        return num

def str_to_int(num):
    if isinstance(num, str):
        value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        result = 0
        for digit in num:
            result = 10 * result + value[digit]
        return result
    else:
        return num


print(int_to_str(4))
print(int_to_str('5'))
print(str_to_int('6'))
print(str_to_int(7))