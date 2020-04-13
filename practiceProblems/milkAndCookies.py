# Is it Time for Milk and Cookies?
# site: https://edabit.com/challenge/6nSckbgCx9hjTwmcw
# Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for Santa! Create a function
# that accepts a Date object and returns True if it's Christmas Eve (December 24th) and False otherwise.
import datetime


def time_for_milk_and_cookies(date):
    indate = date
    christmasdate = datetime.datetime(2020, 12, 24)
    if indate.strftime("%m") == christmasdate.strftime("%m") and indate.strftime("%d") == christmasdate.strftime("%d"):
        print("true")
    else:
        print("false")


time_for_milk_and_cookies(datetime.date(2013, 12, 24))
time_for_milk_and_cookies(datetime.date(2013, 1, 23))
time_for_milk_and_cookies(datetime.date(3000, 12, 24))
