import requests

request = requests.get('https://api.github.com')

if request.status_code == 200:
    print('Success!')
elif request.status_code == 400:
    print('Error!')