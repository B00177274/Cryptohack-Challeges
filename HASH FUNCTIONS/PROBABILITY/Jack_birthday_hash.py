n = 1 << 11
P = 1
for i in range(1, n):
    P = pow((1 - 1/n), i)
    nP = 1 - P
    if nP > 0.5:
        print(i)
        break




    #Solution
    #The code calculates a value based on a series of iterations, adjusting a probability with each step. 
    # It checks if the calculated probability exceeds a threshold of 0.5. 
    # Once this condition is met, the loop stops and outputs the current iteration number.