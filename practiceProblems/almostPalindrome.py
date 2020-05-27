# Almost Palindrome
# site: https://edabit.com/challenge/APNhiaMCuRSwALN63
# A string is an almost-palindrome if, by changing only one character, you can make it a palindrome. Create a function
# that returns True if a string is an almost-palindrome and False otherwise.


def almost_palindrome(txt):
    different = 0
    halflength = len(txt)/2
    backcheck = len(txt)
    for x in range(int(halflength)):
        if txt[x] != txt[int(backcheck)-1]:
            different += 1
        backcheck -= 1
    if different >= 2:
        return False
    else:
        return True


print(almost_palindrome("abcdcbg"))
print(almost_palindrome("abccia"))
print(almost_palindrome("abcdaaa"))
print(almost_palindrome("1234312"))
