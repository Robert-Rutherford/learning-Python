# Friday the 13th
# site: https://edabit.com/challenge/Xkc2iAjwCap2z9N5D
# Given the month and year as numbers, return whether that month contains a Friday 13th.
import datetime


def has_friday_13(month, year):
    date = datetime.datetime(year, month, 13)
    if date.strftime("%A") == 'Friday':
        return True
    else:
        return False


print(has_friday_13(3, 2020))
print(has_friday_13(10, 2017))
print(has_friday_13(1, 1985))
