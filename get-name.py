#!/usr/bin/python
import sys
import json
import urllib.request

html = urllib.request.urlopen("http://localhost:5000/getNameByHostname/"+sys.argv[1]).read()
jsonResponse = json.loads(html.decode('utf-8'))

jsonDump = json.dumps(jsonResponse, indent=1)
jsonDump = jsonDump.replace("\"", "")
jsonDump = jsonDump.replace("{", "")
jsonDump = jsonDump.replace("}", "")
jsonDump = jsonDump.replace(",", "")

print(jsonDump)
input("Press Enter...")