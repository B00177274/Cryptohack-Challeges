a = 26513
b = 32321

if a < b:
    a, b = b, a

r1, r2 = a, b
s1, s2 = 1, 0
t1, t2 = 0, 1

while r2 > 0:
    q, r = divmod(r1, r2)
    r1, r2 = r2, r
    s1, s2 = s2, s1 - q * s2
    t1, t2 = t2, t1 - q * t2

print(f"GCD:{r1}, u:{t1}, v:{s1}")


#Solution
#This code implements the Extended Euclidean Algorithm to compute the greatest common divisor (GCD) of two numbers (a and b) and also finds the coefficients (u and v).

#It uses iterative updates to track the remainders (r1, r2), quotients, and coefficients (s1, s2, t1, t2) until the remainder becomes zero, indicating that the GCD has been found.

#When executed, the script outputs the GCD and the values of u and v, which can be useful in modular arithmetic and cryptographic computations.