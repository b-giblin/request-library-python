# Look more at the req and res objects

import requests



# manipulating headers

# specific exceptions

# using authentication

# ignore ssl warnings

# using sessions 

url = 'https://api.github.com'
c = {
    'test_cookie': 'say something random'
}

h = {
    'User-agent': 'Mozilla/5.0'
}

response = requests.get(
    url,
    
)

response = requests.get(url)
code = response.status_code

# determine the 
if code == 200:
    print(f"Success! Status Code: {response}")
    print(response.text)
elif code == 404:
    print(f"Not Found: {response}")

