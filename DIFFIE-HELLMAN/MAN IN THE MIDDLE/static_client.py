import json
from pwn import *
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

def is_pkcs7_padded(message):
  padding = message[-message[-1]:]
  return all(padding[i] == len(padding) for i in range(0, len(padding)))


con=remote('socket.cryptohack.org',13373,level='debug')
con.recvuntil(b'Intercepted from Alice: ')
alice=json.loads(con.recvline())
p_hex,g_hex,A_hex=alice['p'],alice['g'],alice['A']
con.recvuntil(b'Intercepted from Bob: ')
B_hex=json.loads(con.recvline())['B']
con.recvuntil(b'Intercepted from Alice: ')
content=json.loads(con.recvline())
iv_hex,enc_flag_hex=content['iv'],content['encrypted']
to_bob={"p":p_hex,"g":A_hex,"A":'0x1'}
con.sendline(json.dumps(to_bob))
con.recvuntil(b'Bob says to you: ')
shared_secret=int(json.loads(con.recvline())['B'],16)
con.recvline()

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

print(decrypt_flag(shared_secret,iv_hex, enc_flag_hex))

#Solution
#This script is designed to exploit a vulnerability in an AES encryption scheme that uses Diffie-Hellman key exchange to generate a shared secret for encrypting a flag. The script interacts with a remote service that involves Alice and Bob exchanging Diffie-Hellman parameters and public keys. 
#It first manipulates the Diffie-Hellman exchange by sending a crafted message to Bob, then it retrieves the shared secret B that can be used to decrypt the flag. 
#The decrypt_flag function uses the shared secret, the IV (initialization vector), and the encrypted flag to compute the AES key, decrypt the message, and return the decrypted flag.
