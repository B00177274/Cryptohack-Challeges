ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485
hexed_ct = hex(ct)

flag = bytearray.fromhex(hexed_ct[2:]).decode()

print(flag)


#Solution
#The code begins by converting the given ciphertext (ct) into a hexadecimal string using the hex() function.
#  It then slices off the first two characters of the hexadecimal string (which represent "0x") and decodes the remaining string into a bytearray. 
# This bytearray is then interpreted as a flag, presumably in a human-readable format.
#  Finally, the decoded flag is printed out, showing the result of the decryption or conversion.