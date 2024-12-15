import requests
import json
from pwn import *

url = 'http://aes.cryptohack.org/symmetry/'

def encrypted_flag():
    r = requests.get(url + "encrypt_flag/")
    eflag = r.json()['ciphertext']
    return eflag

def encrypt(plain, iv):
    r = requests.get(url + "encrypt/" + plain + "/" + iv + "/")
    res = r.json()['ciphertext']
    return res

ef = encrypted_flag()
iv = ef[:32]
cip = ef[32:]

ret = encrypt(cip, iv)
print(bytes.fromhex(ret))


#solution
#The script interacts with a web service to retrieve and manipulate AES-encrypted data. 
# It first fetches an encrypted flag, which consists of a ciphertext and an initialization vector (IV).
#  The script then attempts to re-encrypt the ciphertext using the same IV, leveraging the web service's encryption endpoint. 
# The output of this process is printed in bytes, likely for further analysis or decryption attempts.