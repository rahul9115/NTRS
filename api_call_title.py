import requests

headers = {
    'accept': 'application/json',
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}

json_data = {
    'stiType': 'THESIS_DISSERTATION',
    "downloadsAvailable": "true"

}

response = requests.post('https://ntrs.nasa.gov/api/citations/search', headers=headers, json=json_data)

json_response=response.json()
results=json_response["results"]
ids=[]
title=[]
abstract=[]
sub_categories=[]
for i in results:
    ids.append(i["id"])
    
    
    