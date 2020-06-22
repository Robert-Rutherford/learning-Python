# A Subtle Switcheroo
# site: https://edabit.com/challenge/o7u9hqTW5AY3SoZgT
# Create a function which replaces all instances of "nts" with "nce" and vice versa if they are at the end of a word.


def switcheroo(txt):
    words = txt.split()
    special_characters = ['.', ',', '?', '!', '/']
    words_array = list()
    for word in words:
        if len(word) >= 3:
            last_letter = -1
            special = True
            while special:
                if word[last_letter] in special_characters:
                    last_letter -= 1
                else:
                    special = False
            front_letters = word[:(last_letter - 2)]
            remainder = ""
            if last_letter == -1:
                end_letters = word[(last_letter - 2):]
            else:
                end_letters = word[(last_letter - 2): (last_letter+1)]
                remainder += word[last_letter:]
            new_word = ""
            if end_letters == "nts":
                new_word = new_word + front_letters + "nce" + remainder
            elif end_letters == "nce":
                new_word = new_word + front_letters + "nts" + remainder
            else:
                new_word += word
            words_array.append(new_word)
        else:
            words_array.append(word)
    return " ".join(words_array)


print(switcheroo("The elephants in France were chased by ants!"))
print(switcheroo("While he rants, I fall into a trance..."))
print(switcheroo("Bounced over the fence!"))
print(switcheroo(""))
