"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Number of primes must be greater than 0")
    list = []
    i = 2
    while(len(list) < number_of_primes):
        isPrime = True
        for j in range(2, i):
            if(i % j == 0):
                isPrime = False
                break
        if isPrime:
            list.append(i)
        i += 1

    return list
