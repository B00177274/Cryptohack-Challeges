from Crypto.Util.number import bytes_to_long, long_to_bytes, isPrime, inverse
from pwn import *
from json import loads, dumps
from sympy import nextprime
from array import array
from hashlib import md5

input1 = array('I',  [0x6165300e,0x87a79a55,0xf7c60bd0,0x34febd0b,0x6503cf04,0x854f709e,0xfb0fc034,0x874c9c65,0x2f94cc40,0x15a12deb,0x5c15f4a3,0x490786bb,0x6d658673,0xa4341f7d,0x8fd75920,0xefd18d5a])
input2 = array('I', [x^y for x,y in zip(input1,[0, 0, 0, 0, 0, 1<<10, 0, 0, 0, 0, 1<<31, 0, 0, 0, 0, 0])])

input1 = bytes(input1)
input2 = bytes(input2)
assert md5(input1).hexdigest() == md5(input2).hexdigest()
prime = nextprime(256**2 * bytes_to_long(input1))
suffix = prime - 256**2 * bytes_to_long(input1)

input1 += b'\x00' + suffix.to_bytes()
non_prime = bytes_to_long(input2 + b'\x00' + suffix.to_bytes())
print(non_prime)
# dùng factordb để tìm ước của non_prime
a = 367 
r = remote("socket.cryptohack.org", 13392)
send = dumps({"option" : "sign", "prime" : prime}).encode()
_ = r.recvline()
r.sendline(send)

sign = loads(r.recvline().decode())['signature']
print(sign)
send = dumps({"option" : "check", "prime" : non_prime, "signature" : sign, "a" : a}).encode()
r.sendline(send)
r.interactive()

#Solution
#The code imports various cryptographic and mathematical libraries and defines two arrays, input1 and input2, containing 16 elements each. 
# The elements of input2 are derived by XORing corresponding values of input1 with a mask, and then both input1 and input2 are converted to bytes. 
# The code then ensures that the MD5 hash of input1 matches the hash of input2. 
# It computes a prime number based on the value of input1 and calculates a suffix that, when appended to input1, ensures the value of input2 is not prime. 
# Finally, the script interacts with a remote server, signing a prime number and checking the validity of the signature for a non-prime number, then enters interactive mode with the server.