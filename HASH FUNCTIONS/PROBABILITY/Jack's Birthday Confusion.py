from math import factorial
n = 2048
for i in range(n):
	probability = 1 - factorial(n) / (factorial(n - i)*pow(n,i))
	if probability > 0.75:
		print(i)
		break


	#Solution
	#The code calculates a probability using the factorial formula for combinations in each iteration.
	 #It checks if the probability exceeds a threshold of 0.75. 
	 #The loop stops as soon as this condition is met, and the current iteration number is printed. 
	 #The goal is to determine the iteration at which the probability becomes greater than 0.75.