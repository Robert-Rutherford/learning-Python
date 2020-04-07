# Problem: Alphabet Soup
# site: https://edabit.com/challenge/4Agr8CTY7x2rAhh5n
# task: Create a function that takes a string and returns a string with its letters in alphabetical order.
def alphabet_soup(txt):
    # sorttxt = sorted(txt)
    str = ""
    print(str.join(sorted(txt)))


alphabet_soup("hello")
alphabet_soup("edabit")
alphabet_soup("hacker")
alphabet_soup("geek")
alphabet_soup("javascript")
