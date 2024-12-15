#!/usr/bin/env python3
import time
import requests
import string

def print_blk(hex_blks, sz):
   for i in range(0, len(hex_blks), sz):
       print(hex_blks[i:i+sz], ' ', end='')
   print()

def encrypt(plain):
    url = 'http://aes.cryptohack.org/ctrime/encrypt/'
    rsp = requests.get(url + plain + '/')
    return rsp.json()['ciphertext']

alphabet = '}'+'!'+'_'+'@'+'?'+string.ascii_uppercase+string.digits+string.ascii_lowercase

def bruteforce():
    
    flag = b'crypto{'
    cipher = encrypt(flag.hex())
    mi = len(cipher)

    while True:
        for c in alphabet:
            cipher = encrypt((flag+c.encode()).hex())
            print(c, len(cipher))
            if mi == len(cipher):
                flag += c.encode()
                mi = len(cipher)
                print(mi, flag)
                break
            if c == alphabet[-1]:
                mi += 2
                break
            time.sleep(1)

        if flag.endswith(b'}'): 
            print(flag)
            break

bruteforce()


#Solution
#The code is a brute-force solution to decrypt the flag from an AES-CTR encryption challenge. 
# It starts with the known partial flag crypto{, then iterates over a custom alphabet to guess each subsequent character. 
# The encrypt function is used to send the current flag as a hex-encoded string and retrieve the corresponding ciphertext. 
# The brute-force process checks if the ciphertext length remains constant to determine if the correct character has been added, seventually revealing the full flag enclosed in }.