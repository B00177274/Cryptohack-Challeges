def gcd(a, b):
    while a % b != 0:
        c = a % b
        a = b
        b = c
    return b

print(gcd(66528, 52920))


#Solution
#The code defines a function gcd that calculates the greatest common divisor (GCD) of two numbers (a and b) using the Euclidean Algorithm, which repeatedly replaces the larger number with its remainder until the remainder becomes zero.

#Inside the function, the remainder is computed using the modulus operator (%), and the process continues iteratively until the GCD is determined and returned as the last non-zero remainder.

#When executed with inputs 66528 and 52920, the script calculates and prints their GCD, which is 1512.