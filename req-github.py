import requests
from requests.exceptions import *
from gtoken import get_token

# variables
token = get_token
user = 'b-giblin'
auth_header = (user, token)
base_url = 'https://api.github.com/'
header = {
    'Authorization': 'token ' + token
}

#actionable code
res = requests.get(f"{base_url}user", headers=header)
print(res.json())