import requests
from Crypto.Util.number import long_to_bytes

URL = "http://aes.cryptohack.org/ecbcbcwtf/"

# request ciphertext/encrypted flag
r = requests.get(URL + "encrypt_flag")
res = r.json()['ciphertext']
iv = res[:32]

flag = ""

# decrypting the flag
for i in range(1,3):
    cipher = res[32*i:32*(i+1)]
    plain = requests.get(URL + "decrypt/" + cipher)
    resp = plain.json()['plaintext']
    res1 = hex(int(resp,16) ^ int(iv, 16))[2:]
    # print(long_to_bytes(int(res1, 16)))
    flag = flag + res1
    iv = cipher

print(long_to_bytes(int(flag, 16)))


#Solution
#The code sends a request to an AES encryption service to retrieve an encrypted flag.
#  It extracts the Initialization Vector (IV) and decrypts the ciphertext in blocks, using the previous block's ciphertext as the new IV. 
# The decrypted data is XORed with the IV to recover the original plaintext flag. 
# Finally, the flag is printed by converting the result from hexadecimal to bytes.