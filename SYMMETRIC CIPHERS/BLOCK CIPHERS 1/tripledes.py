import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long

def encrypt(key, plain):
    url = "http://aes.cryptohack.org/triple_des/encrypt/"
    url += key
    url += "/"
    url += plain.hex()
    url += "/"
    r = requests.get(url).json()
    return bytes.fromhex(r["ciphertext"])

def encrypt_flag(key):
    url = "http://aes.cryptohack.org/triple_des/encrypt_flag/"
    r = requests.get(url + key + '/').json()
    return bytes.fromhex(r["ciphertext"])

key = b'\x00'*8 + b'\xff'*8
flag = encrypt_flag(key.hex())
cipher = encrypt(key.hex(), flag)
print(cipher)


#Solution
#The Python script encrypts a flag using the Triple DES (3DES) encryption algorithm.
#  It first defines two functions: encrypt() for encrypting arbitrary data with a given key, and encrypt_flag() for retrieving the encrypted flag using a fixed key. The key used is a combination of 8 bytes of zeros followed by 8 bytes of ones. 
# The script encrypts the flag twice, first retrieving the encrypted flag and then encrypting it again with the provided key, printing the final ciphertext.