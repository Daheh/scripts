#!/usr/bin/python3
from cmd import Cmd
import pprint as pp
import requests
import json

#use api within prompt, taken from htb Zipper ippsec ~ 50:00 #not tested
#api is at: https://www.zabbix.com/documentation/3.0/manual/api/reference/usergroup/object#user_group

class Terminal(Cmd):
	prompt ='> '
	
	def __init__(self):
		self.auth = self.do_login("zapper zapper)
		Cmd.__init__(self)
		
	def api_call(self, method, params, auth, id):
		url = 'http://1.1.1.1/zabbix/api_jsonrpc.php'
		header = { "content-type" : "application/json", }
		payload = { 
				"jsonrpc": "2.0",
				"method": method,
				"params": params,
				"auth": auth,
				"id": id
				}
		response = requests.post(url, data=json.dumps(payload), headers=(header))
		return response.json()
					
	def do_login(self, args):
		user, password = args.split()
		params = {
			"user" : user,
			"password": password,
			}
		auth = self.api_call("user.login", params, None, 0)
		return auth['result']
		
	def do_getGroups(self, args):
		params = {
				"status": 0,
				}
		output = self.api_call("usergroup.get", params, self.auth, 0)
		pp.pprint(output)
						
	def do_getUsers(self, args):
		params = {
			"getAccess":1,
			}
		output = self.api_call("user.get", params, auth, 0)
		pp.pprint(output)

	def do_makeAdmin(self, args):
		params = {
				"userid":args,
				"type": 3,
				}
		output = self.api_call("user.update", params, self.auth, 0)
		pp.pprint(output)
		
	def do_createUser(self, args):
		user,password = args.split()
		params = {
				"alias" : user,
				"name" : user,
				"passwd": password,
				"usrgrps": [ { "usrgrpid": "7" } ]
				}
		output = self.api_call("user.create", params, self.auth, 0)
		pp.pprint(output)
						
	def do_subscribe(self,args):
		print(self.auth)
		
terminal = Terminal()
terminal.cmdloop()


"""
example for zipper htb machine
#use api within prompt, taken from htb Zipper ippsec ~ 50:00 #not tested
#api is at: https://www.zabbix.com/documentation/3.0/manual/api/reference/usergroup/object#user_group

class Terminal(Cmd):
	prompt ='> '
	
	def __init__(self):
		self.auth = self.do_login("zapper zapper)
		Cmd.__init__(self)
		
	def api_call(self, method, params, auth, id):
		url = 'http://1.1.1.1/zabbix/api_jsonrpc.php'
		header = { "content-type" : "application/json", }
		payload = { 
				"jsonrpc": "2.0",
				"method": method,
				"params": params,
				"auth": auth,
				"id": id
				}
		response = requests.post(url, data=json.dumps(payload), headers=(header))
		return response.json()
					
	def do_login(self, args):
		user, password = args.split()
		params = {
			"user" : user,
			"password": password,
			}
		auth = self.api_call("user.login", params, None, 0)
		return auth['result']
		
	def do_getGroups(self, args):
		params = {
				"status": 0,
				}
		output = self.api_call("usergroup.get", params, self.auth, 0)
		pp.pprint(output)
						
	def do_getUsers(self, args):
		params = {
			"getAccess":1,
			}
		output = self.api_call("user.get", params, auth, 0)
		pp.pprint(output)

	def do_makeAdmin(self, args):
		params = {
				"userid":args,
				"type": 3,
				}
		output = self.api_call("user.update", params, self.auth, 0)
		pp.pprint(output)
		
	def do_createUser(self, args):
		user,password = args.split()
		params = {
				"alias" : user,
				"name" : user,
				"passwd": password,
				"usrgrps": [ { "usrgrpid": "7" } ]
				}
		output = self.api_call("user.create", params, self.auth, 0)
		pp.pprint(output)
						
	def do_subscribe(self,args):
		print(self.auth)
		
terminal = Terminal()
terminal.cmdloop()



"""
