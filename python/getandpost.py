#!/usr/env/bin python
import requests
from pprint import pprint
from bs4 import BeautifulSoup
import os
import sys
import hashlib
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


cookies = {
	'PHPSESSID':'kv0u5topgio5vik5okova13dn5'
}

headers = {
	'Host': '46.101.33.243:30956',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Upgrade-Insecure-Requests': '1',
	'Connection': 'close',
}

data = {
	
}

response = requests.get('http://46.101.33.243:30956/', headers=headers, cookies=cookies, data=data)
print(response.status_code)
print(response.text)
soup=BeautifulSoup(response.text)
heading = soup.find('h3')

heading_data = heading.text
print(heading_data)
m =hashlib.md5()
m.update(heading_data)
md5hash = m.hexdigest()



cookies = {
	'PHPSESSID':'kv0u5topgio5vik5okova13dn5'
}

headers = {
	'Host': '46.101.33.243:30956',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Content-Length': '9',
	'Upgrade-Insecure-Requests': '1',
	'Origin': 'http://46.101.33.243:30956',
	'Connection': 'close',
	'Referer': 'http://46.101.33.243:30956/',
	
}

data = {
	'hash':md5hash
}
response = requests.post('http://46.101.33.243:30956/', headers=headers, cookies=cookies, data=data)
print(response.text)

