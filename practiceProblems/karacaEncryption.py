# The Karaca's Encryption Algorithm
# site: https://edabit.com/challenge/JzBLDzrcGCzDjkk5n
# Make a function that encrypts a given input with these steps:
#
# Input: "apple"
#
# Step 1: Reverse the input: "elppa"
#
# Step 2: Replace all vowels using the following chart:
#
# a => 0
# e => 1
# o => 2
# u => 3
#
# # "1lpp0"
# Step 3: Add "aca" to the end of the word: "1lpp0aca"
#
# Output: "1lpp0aca"


def encrypt(word):
    wordreverse = reversed(word)
    encoded = ""
    for letter in wordreverse:
        if letter == "a" or letter == "A":
            encoded = encoded + "0"
        elif letter == "e" or letter == "E":
            encoded = encoded + "1"
        elif letter == "o" or letter == "O":
            encoded = encoded + "2"
        elif letter == "u" or letter == "U":
            encoded = encoded + "3"
        else:
            encoded = encoded + letter
    return encoded + "aca"


print(encrypt("banana"))
print(encrypt("karaca"))
print(encrypt("burak"))
print(encrypt("alpaca"))
