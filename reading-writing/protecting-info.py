import json

with open('credentials.json', 'r') as cred_file:
    creds = cred_file.read()
    print(type(creds))
    cred_file.close()