# Generating Words from Names
# site: https://edabit.com/challenge/sDvjdcBrbHoXKvDsZ
# Write a function that returns True if a given name can generate an array of words.
# Each letter in the name may only be used once.
# All letters in the name must be used.


def anagram(name, words):
    namelist = list()
    for letter in name:
        if letter != " ":
            namelist.append(letter.lower())
    for word in words:
        for lett in word:
            if lett.lower() in namelist:
                namelist.remove(lett)
            else:
                return False
    if len(namelist) > 0:
        return False
    else:
        return True


print(anagram("Justin Bieber", ["injures", "ebb", "it"]))
print(anagram("Natalie Portman", ["ornamental", "pita"]))
print(anagram("Chris Pratt", ["chirps", "rat"]))
print(anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]))
