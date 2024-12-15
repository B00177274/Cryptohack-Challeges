from pwn import xor
import binascii

text = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

# pkey = xor(text[:7], "crypto{") 
# print(pkey.decode()) => myXORke --> myXORkey
pkey = "myXORkey"


key = (pkey * (len(text)//len(pkey)+1))[:len(text)]

flag = xor(text, key)

print(flag.decode('utf-8'))

#Solution
#The code takes a hexadecimal string (text), converts it into bytes, and then uses a pre-determined key (pkey = "myXORkey") to perform a bitwise XOR operation between the text and the key. 
# The key is repeated as many times as needed to match the length of the text, ensuring that the XOR operation works correctly for each byte of the input. 
# After XORing the text with the key, the resulting decoded string is printed, which should reveal the original message or "flag" hidden in the XORed text.