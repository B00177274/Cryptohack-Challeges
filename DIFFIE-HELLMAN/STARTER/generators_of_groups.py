def is_generator(k, p):
  for n in range(2, p):
    if pow(k, n, p) == k:
      return False
  return True

p = 28151
for k in range(p):
  if is_generator(k, p):
    print(k)
    break



#solution
#This code searches for a primitive root modulo a prime number 
#𝑝
#p. It defines a function that checks if a given number 
#𝑘
#k is a generator by calculating its powers modulo 
#𝑝
#p and ensuring that none of them repeat prematurely. The loop iterates through possible values of 
#𝑘
#k to find the first number that satisfies the condition of being a generator. If a generator is found, the program prints the value and stops searching.
