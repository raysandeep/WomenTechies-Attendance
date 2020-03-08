import requests
import json

import csv 
filename = "full_details.csv"
filename1 = "details1.csv"

fields = [] 
rows = [] 
fields1 = [] 
rows1 = [] 


def func(email,password,name,regis,phone,block):
    url = "http://127.0.0.1:8000/auth/users/"

    payload = 'username='+email+'m&password='+password
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))


    url = "http://127.0.0.1:8000/auth/token/login"

    payload = 'username='+email+'m&password='+password
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text)
    json_data = json.loads(response.text)

    token = json_data['auth_token']
    print(token)
    url = "http://127.0.0.1:8000/api/"

    payload = 'name='+name+'&regis='+regis+'&email='+email+'&block='+block+'&agreement=False'
    headers = {
    'Authorization': 'Token '+token,
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))




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


def get_pass(id):
    return rows1[id][4]
def get_email(id):
    return rows1[id][1]


print(rows1[2][4])
num = len(rows)
print('\n\nRows are') 
i=0
for row in rows[1:num]: 

    func(get_email(i),get_pass(i),row[1],str(0),row[9],row[8])
    i+=1
print('done')