# Words With Duplicate Letters
# site: https://edabit.com/challenge/WS6hR6b9EZzuDTD26
# Given a common phrase, return False if any individual word in the phrase contains duplicate letters.
# Return True otherwise.


def no_duplicate_letters(phrase):
    splitphrase = phrase.split(" ")
    for word in splitphrase:
        start = 1
        for letter in word:
            if start < len(word):
                for compareletter in word[start:]:
                    if letter.lower() == compareletter.lower():
                        return False
            start = start + 1
    return True


print(no_duplicate_letters("Fortune favours the bold."))
print(no_duplicate_letters("You can lead a horse to water, but you can't make him drink."))
print(no_duplicate_letters("Look before you leap."))
print(no_duplicate_letters("An apple a day keeps the doctor away."))
