# TOPdeskCLI-Python-Scripts

Some TOPdesk python scripts that help with fetching computer names by username or usernames by computername directly on the console.

# api.py : JSON-API using Flask.
Get Hostname by Name:
Example: http://server/getHostnameByName/Miller
Returns:
{

    "description": "Latitude E7440",
    "hostname": "NB2121",
    "location": "IT Department",
    "username": "Miller, James"

}

Get Name by Hostname:
Example: http://server/getNameByHostname/NB2121
Returns:
{

    "description": "Latitude E7440",
    "hostname": "NB2121",
    "location": "IT Department",
    "username": "Miller, James"

}

# get-name.py : Python script consuming the JSON-API
Example: ./get-name.py NB2121

# get-pc.py : Python script consuming the JSON-API
Example: ./get-pc.py Miller