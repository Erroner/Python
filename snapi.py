
import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d - %H:%M:%S')

class Incident:
    def __init__(self, inc_number, inc_ci, inc_type, inc_team, inc_description):
        self.inc_number = inc_number
        self.inc_number = inc_ci
        self.inc_type = inc_type
        self.inc_team = inc_team
        self.inc_description = inc_description

def get_incidents():
    logging.info(f'API request: Initializing')
#url = 'https://yourInstance.service-now.com/api/now/table/'
#headers = {"Content-Type":"application/json","Accept":"application/json"}
#response = requests.get(url, auth=('admin', 'admin'), headers=headers )
#if response.status_code != 200: 
#    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
#    exit()
    with open("get_incidents.json", 'r') as f:
        get_incidents_response = json.load(f)
    logging.info(f'API request: Data gathered')
    return get_incidents_response
    

def sort_incidents(response):
    logging.info(f'INC classifying: JSON loaded')    
    inc_sorted = []
    for inc_part in response.get("result", []):
        if "Node down" in inc_part["short description"]:
            inc_type = "node_down"
        elif "discards" in inc_part["short description"]:
            inc_type = "discards"
        elif "disk utilization" in inc_part["short description"]:
            inc_type = "disk_utilization"

        inc_parts = {
            "inc_number": inc_part['number'],
            "inc_type": inc_type,
            "inc_team": inc_part['assignment group'],
            "inc_title": inc_part['short description'],
            "inc_ci": inc_part['configuration item'],
            "inc_description": inc_part['description']}
        inc_sorted.append(inc_parts)

        if "Node down" in inc_part["short description"]:
            inc_part["inc_type"] = "node_down"

    logging.info(f'INC classifying: Incidents classified')        
    print(inc_sorted)
    return inc_sorted

sort_incidents(get_incidents())




