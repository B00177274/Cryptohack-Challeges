from pwn import *
import json
msg1 = open('message1.bin', 'rb').read()
msg2 = open('message2.bin','rb').read()
r = remote("socket.cryptohack.org", 13389)

payload1 = {
	'document' : msg1.hex()
}

payload2 = {
	'document' : msg2.hex()
}
payload1 = json.dumps(payload1).encode()
payload2 = json.dumps(payload2).encode()

r.sendlineafter(b'store\n', payload1)
r.sendlineafter(b'\n', payload2)
print(r.recvline())
r.close()


#Solution
#The code reads two binary files, message1.bin and message2.bin, and converts their contents to hexadecimal format. 
# It then creates JSON payloads where the hex-encoded binary data is associated with the key 'document'.
#  These payloads are serialized into JSON and encoded as bytes. 
# The code establishes a connection to a remote server using pwn's remote() function, sending the payloads one after the other. 
# Finally, it prints the server's response and closes the connection.