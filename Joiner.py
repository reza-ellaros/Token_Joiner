import requests
from colorama import Fore, Style, init

url = input("Invite Code : ")
invite = url.split("/")[-1]

api_url = "https://discord.com/api/v9/invites/" + invite

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
                
            requests.post(url, headers=headers)
        print ("joined!")

input()