#!/usr/bin/env python3

#!/usr/bin/env python3

import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 11112

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


print(readline())
print(readline())
print(readline())
print(readline())


request = {
    "buy": "Flag"
}
json_send(request)

response = json_recv()

print(response)


#Solution
#The code connects to a remote server using the telnetlib library on port 11112 of the host socket.cryptohack.org. 
# It defines functions to read the response from the server and send JSON-encoded requests. 
# The script first reads and prints four lines of responses from the server using the readline() function. 
# Then, it sends a JSON request with the key "buy" and value "Flag", and prints the response from the server, which presumably contains the flag or additional information
