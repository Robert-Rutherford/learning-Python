# Find ASCII Charcode of Inverse Case Character
# site: https://edabit.com/challenge/QFXMcwaQZ8FTAuEtg
# Create a function that takes a single character as an argument and returns the char code of its lowercased /
# uppercased counterpart.


def counterpartCharCode(char):
    if char.isupper():
        return ord(char.lower())
    elif char.islower():
        return ord(char.upper())
    else:
        return ord(char)


print(counterpartCharCode("A"))
print(counterpartCharCode("a"))
