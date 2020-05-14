# C*ns*r*d Str*ngs
# site: https://edabit.com/challenge/ehyZvt6AJF4rKFfXT
# Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able
# to find the vowels that were removed.
#
# Given a censored string and a string of the censored vowels, return the original uncensored string.


def uncensor(txt, vowels):
    position = 0
    returntxt = ""
    for letters in txt:
        if letters == "*":
            returntxt += vowels[position]
            position += 1
        else:
            returntxt += letters
    return returntxt


print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor("abcd", ""))
print(uncensor("*PP*RC*S*", "UEAE"))
