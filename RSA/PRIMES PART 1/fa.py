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
