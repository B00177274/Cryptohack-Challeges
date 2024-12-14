from pwn import *
import json
block1 = b'a'*32
block2 = b'b'*32

m1 = (block1 + block2).hex()
m2 = (block2 + block1).hex()
payload = json.dumps({"m1" : m1, "m2" : m2}).encode()
r = remote("socket.cryptohack.org", 13405)
r.sendlineafter(b'in JSON: ', payload)
data = r.recvline()
print(data)
r.close()


#Solution
#The code imports the pwn library to interact with a remote service. 
# It creates two blocks of data, block1 and block2, each filled with 32 bytes of a and b, respectively. 
# These blocks are concatenated in two different orders and converted to hexadecimal strings, stored in the variables m1 and m2. 
# The m1 and m2 values are then encoded into a JSON object and sent as a payload to a remote server via a socket connection. 
# Finally, the script waits for a response from the server, prints the received data, and closes the connection.