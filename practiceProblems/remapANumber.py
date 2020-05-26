# Re-Map a Number from One Range to Another
# site: https://edabit.com/challenge/CsvdwQvNe8hYomcwB
# Create a function similar to Processings "map" function (check the Resources tab), in which a value and it's range
# is taken and remapped to a new range.
#
# The function takes 5 numbers:
#
# Value: value
# Range: low1 and high1
# Range: low2 and high2


def remap(value, low1, high1, low2, high2):
    value2 = 0
    value = high1 if value > high1 else value
    value = low1 if value < low1 else value

    inputSpan = high1 - low1
    outputSpan = high2 - low2

    scaledThrust = float(value - low1) / float(inputSpan)

    return low2 + (scaledThrust * outputSpan)


print(remap(7, 2, 12, 0, 100))
print(remap(17, 5, 55, 100, 30))
print(remap(50, 1, 51, 0, 100))