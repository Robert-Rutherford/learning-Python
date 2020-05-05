# Making a Box
# site: https://edabit.com/challenge/dy3WWJr34gSGRPLee
# Create a function that creates a box based on dimension n.


def makeBox(n):
    box = list()
    if n == 1:
        box.append("#")
        return box
    for x in range(1, n+1):
        boxrow = ""
        for y in range(1, n+1):
            if x == 1 or x == n:
                boxrow = boxrow + "#"
            elif y == 1 or y == n:
                boxrow = boxrow + "#"
            else:
                boxrow = boxrow + " "
        box.append(boxrow)
    return box


print(makeBox(5))
print(makeBox(3))
print(makeBox(2))
print(makeBox(1))