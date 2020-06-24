# Concert Seats
# site: https://edabit.com/challenge/xbjDMxzpFcsAWKp97
# Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage
# if it is strictly greater than the number before it.
#
# Everyone can see the front-stage in the example below:
#
# # FRONT STAGE
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 2, 2],
# [5, 5, 5, 5, 4, 4],
# [6, 6, 7, 6, 5, 5]]
#
# # Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# # 6 > 5 > 4 > 2 - so all numbers can see, etc.
# Not everyone can see the front-stage in the example below:
#
# # FRONT STAGE
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 2, 2],
# [5, 5, 5, 10, 4, 4],
# [6, 6, 7, 6, 5, 5]]
#
# # The 10 is directly in front of the 6 and blocking its view.
# The function should return True if every number can see the front-stage, and False if even a single number cannot.


def can_see_stage(seats):
    largest_seats = seats[0]
    for row in seats:
        if row != largest_seats:
            for x in range(len(row)):
                if largest_seats[x] >= row[x]:
                    return False
                else:
                    largest_seats[x] = row[x]
    return True


print(can_see_stage([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
print(can_see_stage([
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
]))
print(can_see_stage([
    [2, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
]))
print(can_see_stage([
    [1, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
]))
