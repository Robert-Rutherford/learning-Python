# Loves Me, Loves Me Not...
# site: https://edabit.com/challenge/6pEGXsuCAxbWTRkgc
# "Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one,
# saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.
#
# Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every
# alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.


def loves_me(n):
    lovelist = ["loves me", "loves me not"]
    quote = ""
    loveme = True
    for x in range(1, n):
        if loveme:
            quote = quote + lovelist[0] + ", "
            loveme = False
        else:
            quote = quote + lovelist[1] + ", "
            loveme = True
    if loveme:
        quote += lovelist[0].upper()
    else:
        quote += lovelist[1].upper()
    return quote


print(loves_me(3))
print(loves_me(6))
print(loves_me(1))
