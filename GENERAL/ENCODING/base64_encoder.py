# Base64 Cryptohack - Windy Arya - 5027201071
import base64
import binascii

hex_val = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

base_val = base64.b64encode(bytes.fromhex(hex_val))
print(base_val.decode('utf-8'))
done = 0;


#Solution
#The code converts a hexadecimal string (hex_val) into its equivalent binary representation using the bytes.fromhex() method.

#This binary data is then encoded into a Base64 string using the base64.b64encode() function, which is a common encoding method for transmitting binary data in a text-safe format.

#The resulting Base64-encoded value is converted to a human-readable string using the decode('utf-8') method and printed to the console.

#The code is useful for tasks that involve encoding data into Base64 for compatibility with systems that cannot handle raw binary data.

#The variable done = 0 is included but serves no functional purpose within the script