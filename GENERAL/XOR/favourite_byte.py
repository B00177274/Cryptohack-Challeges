import binascii

text = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

btext = bytearray.fromhex(text)

for i in range(256):
    result = ''
    for n in btext:
        result += chr(n^i)
    
    if (result.startswith('crypto')):
        print(result)


        #Solution
        #The code takes a hexadecimal string (text) and converts it into a byte array using bytearray.fromhex(). 
        # Then, it iterates through all possible values of i from 0 to 255 and applies an XOR operation (^) between each byte in the byte array and i, converting the result back to characters. 
        # The script checks if the resulting string starts with "crypto", and if so, it prints the decoded string, which suggests that the XOR operation is being used to decode the original message hidden in the hexadecimal string