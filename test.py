import requests
import json

import csv 
filename = "full_details.csv"
filename1 = "details1.csv"

fields = [] 
rows = [] 
fields1 = [] 
rows1 = [] 

email='rayan@gmail.com'
password='manboobs'

BASE_URL = 'https://women-techies.herokuapp.com'

url = BASE_URL+"/auth/users/"

payload = {
    'username':email,
    'password':password
}

headers = {
'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.post(url, headers=headers, data = payload)

print(response.text.encode('utf8'))


url = BASE_URL+"/auth/token/login"

response = requests.post(url, headers=headers, data = payload)

print(response.text)