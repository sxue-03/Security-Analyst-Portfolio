from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
def make_key(password):
    salt = os.urandom(16)
    kdf=PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000)
    key=base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt
def encrypt_file(filename,password):
    key,salt = make_key(password)
    data = open(filename,'rb').read()
    encrypted=Fernet(key).encrypt(data)
    with open(filename,'wb') as f:
        f.write(salt)
        f.write(encrypted)
    print('encrypted:',filename)
def decrypt_file(filename,password):
    data=open(filename,'rb').read()
    salt=data[:16]
    encrypted=data[16:]
    kdf=PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000)
    key=base64.urlsafe_b64encode(kdf.derive(password.encode()))
    decrypted=Fernet(key).decrypt(encrypted)
    with open(filename,'wb')as f:
        f.write(decrypted)
    print('decrypted:', filename)
choice=input('encrypt or decrypt (e/d):')
filename=input('enter file path:')
password=input('enter password:')
if choice == 'e':
    encrypt_file(filename,password)
elif choice == 'd':
    decrypt_file(filename,password)
else:
    print('invalid choice')