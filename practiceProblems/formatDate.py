# Date Format
# site: https://edabit.com/challenge/co4nwXSvnCjGEu8vp
# Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.


def format_date(date):
    datesplit = date.split("/")
    reversedate = [datesplit[2], datesplit[1], datesplit[0]]
    print("".join(reversedate))


format_date("11/12/2019")
format_date("12/31/2019")
format_date("01/15/2019")
