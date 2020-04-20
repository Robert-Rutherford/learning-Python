# Find the Missing Number
# site: https://edabit.com/challenge/oMCNzA4DcgpsnXTRJ
# Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.


def missing_num(lst):
    numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in numlist:
        if num not in lst:
            return num
    return 0


print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))
print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))
