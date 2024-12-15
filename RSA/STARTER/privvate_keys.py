from Crypto.Util.number import inverse

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

tot = (p-1) * (q-1)

print(inverse(e, tot))


#Solution
#The code calculates the modular inverse of e (which is 65537) modulo the totient of N, where N is the product of two large primes p and q. 
# The inverse function from Crypto.Util.number is used to compute the modular inverse. 
# This is typically done in RSA encryption to find the private key d such that d * e ≡ 1 (mod tot). 
# The printed result will be the value of d, which is the modular inverse of e with respect to tot.