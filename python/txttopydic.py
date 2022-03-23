#!/usr/bin/python3
import sys
def txttolist(filename):

	with open(filename, 'r') as f:
		mylist = []
		for line in f:
		    mylist.append(line.strip())
	return mylist
       
if len(sys.argv) < 2:
	print("need filename")
	sys.exit(1)

mylist = txttolist(sys.argv[1])
print(mylist)

