def mod_inv(x, y):
    for i in range(y):
        if (x * i) % y == 1:
            return i

print(mod_inv(3, 13))


#Solution
#The function mod_inv iterates through all integers from 0 to y-1 to find the modular inverse of x modulo y, which is the number i.
 #It checks each integer to see if multiplying x by it and taking the modulo y equals 1, and returns the first such value.
 #  In the example mod_inv(3, 13), the function successfully finds that 9 is the modular inverse of 3 modulo 13.