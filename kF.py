from unittest import result
from pprint import pprint
import requests
import json
import subprocess
import os
import time
import sys

# Get input of domain to check as an argument
url = sys.argv[1]

# Greeting
print ("Hello, welcome to the rep scanner")
print ("So you want to scan " + url + "...")
print ("Let's go.")
time.sleep(3)

#url = input("Please enter the url to analyze\n")

# Check on VirusTotal via API
vt = "https://www.virustotal.com/api/v3/search?query="+ url
xapikey = "4dc4218dc7f46c8b98dd358c7ed0e7655f01d0fbf2ca1f5f0b1f1669861b9f31"

headers = {
    "Accept": "application/json",
    "x-apikey": xapikey
}
response=requests.get(vt, headers=headers)

raw=response.json()
responsevt=response.content #returns the content of the response-

# Write results to a file

file=open('resultVT.json','wb')
file.write(responsevt)                           
file.close

# show results
print("File created with results in VirusTotal and saved as resultVT.json")
print("VT raw result")
print(raw)

# check size
stats = os.stat('resultVT.json')
print('Size of file is', stats.st_size, 'bytes')

# Check on URLScan.io via API
apikey = "0d172568-0023-4e08-ad0c-c287c477d0b2"
headers = {'API-Key':apikey,'Content-Type':'application/json'}
data = {"url": url, "visibility": "public"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))

print(response)
print("urlscan.io raw response:",response.json())

# scrapping in US results
responseus = response.json()
url = responseus['api']
time.sleep(15)

response = requests.get(url)
print(response.url)
responseus = response.content
print(responseus)

# Write json result to a file
file=open('resultUS.json','wb')
file.write(responseus)                           
file.close

print("File created with json results in URLScan.io and saved as resultUS.json")

# check size
stats = os.stat('resultUS.json')
print('Size of file is', stats.st_size, 'bytes')

#calls for my upload to S3 script
import subprocess
subprocess.call(" python3 ups3.py 1", shell=True)