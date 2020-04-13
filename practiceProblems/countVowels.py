# How Many Vowels?
# site: https://edabit.com/challenge/p88k8yHRPTMPt4bBo
# Create a function that takes a string and returns the number (count) of vowels contained within it.


def count_vowels(txt):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for element in txt:
        for vowel in vowels:
            if element.lower() == vowel.lower():
                count = count + 1
    print(count)


count_vowels("Celebration")
count_vowels("Palm")
count_vowels("Prediction")
