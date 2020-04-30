# Stupid Addition
# site: https://edabit.com/challenge/6dnhESWBcTMMF3gsa
# Create a function that takes two parameters and, if both parameters are strings, add them as if they were
# integers or if the two parameters are integers, concatenate them.


def stupid_addition(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return str(a) + str(b)
    elif isinstance(a, str) and isinstance(b, str):
        return int(a) + int(b)
    else:
        return None


print(stupid_addition(1, 2))
print(stupid_addition("1", "2"))
print(stupid_addition("1", 2))
