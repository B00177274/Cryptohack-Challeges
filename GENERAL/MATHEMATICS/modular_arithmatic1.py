x = 11 % 6
y = 8146798528947 % 17

#The smaller integer is the flag
if x > y:
    print(y)
else:
    print(x)



    #Solution

    #The code calculates the remainders when dividing 11 by 6 and 8146798528947 by 17, storing these remainders in variables x and y, respectively. 
    # It then compares x and y to determine which is smaller, with the smaller value being considered the "flag." 
    # In this case, since 4 (the value of y) is smaller than 5 (the value of x), the script prints y, which equals 4