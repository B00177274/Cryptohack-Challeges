from Crypto.PublicKey import RSA
from base64 import b64decode ,b16encode
with open('/home/b00177274/Documents/GIT/Cryptohack-Challeges/GENERAL/DATA FORMATS/pmail.pm', "rb" ) as f:
    kobj = RSA.importKey(f.read())
    print(kobj.d)