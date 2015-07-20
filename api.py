#!/usr/bin/python
from flask import Flask
from flask import jsonify
import json
import pyodbc
try:
    from flask.ext.cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

app = Flask(__name__)
cors = CORS(app)
app.debug = True




#setup db connection to sql server
def init_db():
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=topdesk;DATABASE=TOPDESK_PROD;integrated security=true')
	cursor = cnxn.cursor()
	return cursor

cursor = init_db()

#Get Hostname by Name
#Example: http://server/getHostnameByName/Miller
@app.route('/getHostnameByName/<name>')
def get_hostname_by_name(name):
	userObject = db_get_hostname_by_name(name)
	if type(userObject) is pyodbc.Row:
		return jsonify(hostname=userObject[0],username=userObject[1],location=userObject[2],description=userObject[3])
	else:
		return jsonify()

def db_get_hostname_by_name(name):
	cursor.execute("SELECT [naam], [ref_gebruiker], [ref_lokatie], [objecttype], [specificatie]  FROM [TOPDESK_PROD].[dbo].[hardware] WHERE ref_gebruiker Like '%"+name+"%' ORDER BY naam DESC")
	rows = cursor.fetchall()
	if rows:
		for row in rows:
			if("NB" in row[0]) or ("PC" in row[0]):
				return row
		return rows[0]

#Get Name by Hostname
#Example: http://server/getNameByHostname/PC2219
@app.route('/getNameByHostname/<hostname>')
def get_name_by_hostname(hostname):
	userObject = db_get_name_by_hostname(hostname)
	if type(userObject) is pyodbc.Row:
		return jsonify(username=userObject[0],hostname=userObject[1],location=userObject[2],description=userObject[3])
	else:
		return jsonify()

def db_get_name_by_hostname(hostname):
	#setup db connection to sql
	cursor.execute("SELECT [ref_gebruiker], [naam], [ref_lokatie], [objecttype], [specificatie] FROM [TOPDESK_PROD].[dbo].[hardware] WHERE naam = '"+hostname+"'")
	rows = cursor.fetchall()
	if rows:
		return rows[0]

if __name__ == "__main__":
	app.run(host='0.0.0.0')
