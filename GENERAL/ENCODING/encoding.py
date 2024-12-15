from pwn import * # pip install pwntools
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random
from binascii import unhexlify


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def list_to_string(s):
    output = ""
    return(output.join(s))

for i in range(0,101):
    received = json_recv()
    if "flag" in received:
        print("\n[*] FLAG: {}".format(received["flag"]))
        break

    print("\n[-] Cycle: {}".format(i))
    print("[-] Received type: {}".format(received["type"]))
    print("[-] Received encoded value: {}".format(received["encoded"]))

    word = received["encoded"]
    encoding = received["type"]

    if encoding == "base64":
        decoded = base64.b64decode(word).decode('utf8').replace("'", '"')
    elif encoding == "hex":
        decoded = (unhexlify(word)).decode('utf8').replace("'", '"')
    elif encoding == "rot13":
        decoded = codecs.decode(word, 'rot_13')
    elif encoding == "bigint":
        decoded = unhexlify(word.replace("0x", "")).decode('utf8').replace("'", '"')
    elif encoding == "utf-8":
        decoded = list_to_string([chr(b) for b in word])

    print("[-] Decoded: {}".format(decoded))
    print("[-] Decoded Type: {}".format(type(decoded)))

    to_send = {
        "decoded": decoded
    }

    json_send(to_send)



    #Solution

    #The script interacts with a remote server using pwntools to solve an encoding/decoding challenge, repeatedly receiving encoded data and decoding it based on the specified encoding type.

#It uses various decoding techniques such as Base64 decoding (base64.b64decode), hexadecimal decoding (unhexlify), ROT13 decoding (codecs.decode), BigInteger conversion (unhexlify after stripping "0x"), and UTF-8 character list conversion.

#The json_recv() and json_send() functions handle communication with the server by receiving and sending JSON-formatted data, making the script robust for structured communication.

#The loop runs up to 101 times or until the flag is received from the server, decoding the given data and sending the decoded response back to progress through the challenge.

#The script provides debug information during each cycle, displaying the encoding type, the encoded value, the decoded result, and its type, which aids in understanding the server's response and verifying the decoding logic.