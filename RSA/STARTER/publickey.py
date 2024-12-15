from traceback import print_tb


plain = 12
e = 65537
p = 17
q = 23

n = p * q
print(pow(plain, e, n))


#Solution
#The code performs an encryption operation using the RSA algorithm. 
# It calculates the ciphertext by raising the plaintext (12) to the power of the public exponent e (65537), then taking the result modulo n, where n is the product of two primes p (17) and q (23). 
# This step simulates the encryption of a plaintext message in RSA. 
# The output will be the encrypted ciphertext corresponding to the given plaintext, exponent, and modulus.