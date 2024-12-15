from Crypto.PublicKey import RSA
from base64 import b64decode ,b16encode
with open('/home/b00177274/Documents/GIT/Cryptohack-Challeges/GENERAL/DATA FORMATS/pmail.pm', "rb" ) as f:
    kobj = RSA.importKey(f.read())
    print(kobj.d)


#Solution
#This code imports an RSA private key from a file and prints the private exponent 
#𝑑
#d of the key. It first opens the file containing the RSA key in binary mode, then reads the key and imports it using the RSA.importKey function from the Crypto.PublicKey module. The private exponent 
#𝑑
#d is a crucial part of the RSA private key, used in decryption operations. Finally, the value of 
#𝑑
#d is printed to the console.
