# Filter Primes from a List
# site: https://edabit.com/challenge/yXZhG7zq6dWhWhirt
# Create a function that takes a list and returns a new list containing only prime numbers.


def filter_primes(num):
    primes = list()
    for number in num:
        prime = True
        if number > 1:
            for x in range(2, number):
                if (number % x) == 0:
                    prime = False
            else:
                if prime:
                    primes.append(number)
    return primes


print(filter_primes([7, 9, 3, 9, 10, 11, 27]))
print(filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]))
print(filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]))
