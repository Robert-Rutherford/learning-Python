# Return the Index of All Capital Letters
# site: https://edabit.com/challenge/rQkriLJBc9CbfRbJb
# Create a function that takes a single string as argument and returns an ordered list containing the
# indices of all capital letters in the string.


def index_of_caps(word):
    capindex = []
    index = 0
    for letter in word:
        if letter.isupper():
            capindex.append(index)
        index = index + 1
    print(capindex)


index_of_caps("eDaBiT")
index_of_caps("eQuINoX")
index_of_caps("determine")
index_of_caps("STRIKE")
index_of_caps("sUn")