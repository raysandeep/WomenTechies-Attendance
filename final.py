import requests
import json

import csv 
filename = "full_details.csv"
filename1 = "details1.csv"

fields = [] 
rows = [] 
fields1 = [] 
rows1 = [] 

BASE_URL = 'https://women-techies.herokuapp.com'
def func(email,password,name,block,regis,phone):
    url = BASE_URL+"/auth/users/"

    payload = 'username='+email+'m&password='+password
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))


    url = BASE_URL+"/auth/token/login"

    payload = 'username='+email+'m&password='+password
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text)
    json_data = json.loads(response.text)

    token = json_data['auth_token']
    print(token)
    url = BASE_URL+"/api/"

    payload = 'name='+name+'&regis='+regis+'&email='+email+'&block='+block+'&agreement=False'
    headers = {
    'Authorization': 'Token '+token,
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.status_code)




with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)  
    fields = next(csvreader) 
    for row in csvreader: 
        rows.append(row) 

with open(filename1, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)  
    fields = next(csvreader) 
    for row in csvreader: 
        rows1.append(row)   


def get_pass_phone(id):
    for row1 in rows1:
        if row1[1]==id:
            return row1[4],row1[2]





num = len(rows)
i=0
for row in rows[0:num]: 
    passw,phone=get_pass_phone(row[2])
    print(row[2],passw,row[1],row[8],row[9],phone)
    func(row[2],passw,row[1],row[8],row[9],phone)
print('done')