from math import sqrt


def PrimeFactor(n):
    m = n
    while n % 2 == 0:
        n = n // 2
    if n == 1:
        return 2
    i = 3
    sqrt_m = int(sqrt(m))  # Avoid shadowing the sqrt function
    last = 0
    while i <= sqrt_m:
        while n % i == 0:
            n = n // i
            last = i
        i += 2
    if n > last:  # If n itself is a prime factor larger than last
        return n
    else:
        return last


num = 510143758735509025530880200653196460532653147
print(PrimeFactor(num))

#Solution
#The provided code implements a function to find the largest prime factor of a given number n. 
# It first checks for divisibility by 2, and then iterates over odd numbers up to the square root of n to find other factors.
#  If a factor is found, the number is divided by it, and the process continues until n is no longer divisible by the current factor. 
# The function returns the largest prime factor, either found during the iterations or n itself if it is prime.
