

#!/usr/bin/env python3
from Crypto.Cipher import AES
import requests
import time
import string

def encrypt(payload):
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/"
    r = requests.get(url + payload + '/')
    return r.json()['ciphertext']

def print_blk(hex_blks, sz):
   for i in range(0, len(hex_blks), sz):
       print(hex_blks[i:i+sz], ' ', end='')
   print()

def bruteforce():
    flag = ''
    total = 32 - 1
    alphabet = '_'+'@'+'}'+string.digits+string.ascii_lowercase+string.ascii_uppercase

    while True:
        payload = '1' * (total-len(flag))
        expected = encrypt(payload.encode().hex())
        print('E', '', end='')
        print_blk(expected, 32)
        
        for c in alphabet: 
            res = encrypt(bytes.hex((payload + flag + c).encode()))
            print(c, '', end='')
            print_blk(res, 32)
            if res[32:64] == expected[32:64]:
                flag += c
                print(flag)
                break
            time.sleep(1)

        if flag.endswith('}'): break

    print(flag)

bruteforce()















# Solution:crypto{p3n6u1n5_h473_3cb}
#The provided script attempts to brute-force the flag of a website protected by an AES encryption oracle. 
# It does this by exploiting the ECB (Electronic Codebook) mode, where identical plaintext blocks result in identical ciphertext blocks. 
# The script sends requests to the encryption service, incrementally guessing each character of the flag by comparing the ciphertext block pattern. 
# It stops when the flag matches the expected format, resulting in the final flag, crypto{p3n6u1n5_h473_3cb}.