# First Before Second Letter
# site: https://edabit.com/challenge/D6XfxhRobdQvbKX4v
# You are given three inputs: a string, one letter, and a second letter.
#
# Write a function that returns True if every instance of the first letter occurs before every instance of the
# second letter.


def first_before_second(s, first, second):
    pastfirst = False
    firstconfimed = False
    for letter in s:
        if letter == first:
            if pastfirst is True:
                return False
            else:
                firstconfimed = True
        elif letter == second:
            if firstconfimed is False:
                return False
            else:
                pastfirst = True
    return True


print(first_before_second("a rabbit jumps joyfully", "a", "j"))
print(first_before_second("knaves knew about waterfalls", "k", "w"))
print(first_before_second("happy birthday", "a", "y"))
print(first_before_second("precarious kangaroos", "k", "a"))
