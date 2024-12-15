from pwn import xor	

message = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")


# The resulting XOR is "myXORke". It's safe to assume that the complete word is "myXORkey" thus the additional 'y'
partial_key = xor(message[:7], "crypto{").decode() + 'y'  

complete_key = (partial_key * (len(message)//len(partial_key)+1))[:len(message)]


flag = xor(message, complete_key)

print(flag.decode())

#Solution
#The code attempts to decrypt a message by using a partially known XOR key.

#The message is a hexadecimal string that is first converted into bytes using bytes.fromhex().
#It assumes that the message starts with "crypto{", so the first 7 characters of the message are XORed with "crypto{" to generate a partial key, resulting in "myXORke". Since the key seems to be "myXORkey", an additional 'y' is appended to the partial key.
#The complete key is then extended to match the length of the message by repeating the partial key.
#The message is XORed with the complete key, and the result is decoded and printed, which is expected to reveal the hidden flag or message.