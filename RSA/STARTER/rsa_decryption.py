n = 882564595536224140639625987659416029426239230804614613279163
e = 65537
c = 77578995801157823671636298847186723593814843845525223303932
d = 121832886702415731577073962957377780195510499965398469843281

print(pow(c, d, n))



#solution
#The code is performing a decryption operation using the RSA algorithm. 
# The ciphertext c is raised to the power of the private exponent d, and the result is taken modulo n. 
# This operation will yield the plaintext that was originally encrypted with the public exponent e. 
# The output will be the plaintext message corresponding to the given ciphertext c, private exponent d, and modulus n.