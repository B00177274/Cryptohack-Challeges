import requests

# request encrypted flag
r = requests.get('http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')
res = r.json()['ciphertext']
# print(res)

# request plaintext/decrypting flag
endpointdec = 'http://aes.cryptohack.org/block_cipher_starter/decrypt/' + res
dec = requests.get(endpointdec)
res1 = dec.json()['plaintext']
# print(res1)

by = bytes.fromhex(res1)
finalres = by.decode()
print(finalres)

#solution
#This script interacts with a web service to retrieve and decrypt an AES-encrypted flag.
#  It first requests the encrypted flag from the encrypt_flag endpoint. 
# After receiving the ciphertext, it sends it to the decrypt endpoint to retrieve the plaintext (the original flag). 
# Finally, the script decodes the plaintext from hexadecimal and prints the flag in its readable form.