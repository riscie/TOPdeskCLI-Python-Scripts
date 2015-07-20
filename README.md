# TOPdeskCLI-Python-Scripts

Some TOPdesk python scripts that help with fetching computer names by username or usernames by computername directly on the console.

# api.py * JSON-API using Flask.
<b><u>Get Hostname by Name</u></b>  
<b>Request:</b>   

    http://server/getHostnameByName/Miller  

<b>Answer:</b>

    {
    "description": "Latitude E7440",
    "hostname": "NB2121",
    "location": "IT Department",
    "username": "Miller, James"
    }


<b><u>Get Name by Hostname:</u></b>  
<b>Request:</b>   

    http://server/getNameByHostname/NB2121  

<b>Answer:</b>

    {
    "description": "Latitude E7440",
    "hostname": "NB2121",
    "location": "IT Department",
    "username": "Miller, James"
    }

# get-name.py * Python script consuming the JSON-API   

<b>Example:</b> ./get-name.py NB2121

<b>Answer:</b>  

    hostname: NB2121
    description: Latitude E7440
    username: Miller James
    location: IT Department
    
# get-pc.py * Python script consuming the JSON-API  
<b>Example:</b> ./get-pc.py Miller  

<b>Answer:</b>  

    hostname: NB2121
    description: Latitude E7440
    username: Miller James
    location: IT Department