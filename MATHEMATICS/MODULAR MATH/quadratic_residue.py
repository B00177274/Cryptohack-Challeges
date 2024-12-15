p = 29
ints = [14, 6, 11]

res = []
for a in range(1, p):
    if (a ** 2) % p in ints:
        res.append(a)

print("FLAG =", min(res))
    


#Solution
#The code checks for all numbers a in the range from 1 to p-1, calculates the square of each, and then takes the result modulo p. 
# If the result is present in the given list ints, the number a is added to the list res. 
# Finally, the smallest value from res is printed as the FLAG.
    


