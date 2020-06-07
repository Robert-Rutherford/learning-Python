# Add Two String Numbers
# site: https://edabit.com/challenge/bwCDG9X8cJiAdvfxE
# Write a function that adds two numbers. The catch, however, is that the numbers will be strings.
# Note:
# If there are any non-numerical characters, return "-1".
# If one option is blank the code should still work.
# Python supports the addition of integers without limit, try this challenge without using this functionality.
# Your function doesn't have to add negative numbers.


def add_str_nums(num1, num2):
    number1 = 0
    number2 = 0
    if num1 == "":
        number1 = 0
    elif not num1.isnumeric():
        return "-1"
        # strNumbers = list()
        # for letter in num1:
        #     if letter.isnumeric():
        #         strNumbers.append(letter)
        # if not strNumbers:
        #     number1 = -1
        # else:
        #     number1 = int("".join(strNumbers))
    else:
        number1 = int(num1)
    if num2 == "":
        number2 = 0
    elif not num2.isnumeric():
        return "-1"
        # strNumbers = list()
        # for letter in num2:
        #     if letter.isnumeric():
        #         strNumbers.append(letter)
        # if not strNumbers:
        #     number2 = -1
        # else:
        #     number2 = int("".join(strNumbers))
    else:
        number2 = int(num2)  
    return str(number1 + number2)


print(add_str_nums("4", "5"))
print(add_str_nums("abcdefg", "3"))
print(add_str_nums("1", ""))
print(add_str_nums("1874682736267235927359283579235789257", "32652983572985729"))
