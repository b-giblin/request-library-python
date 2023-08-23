import requests
from requests.exceptions import ConnectionError, HTTPError,Timeout,TooManyRedirects


url = 'https://reddit.com'

try:
    response = requests.get(url)
except ConnectionError:
    print("DNS, refused connection - not due to network issue")
except HTTPError:
    print('This is due to a response code being 4xx, or 5xx')
except Timeout:
    print("The connection timed out, slow server or slow connection")
except TooManyRedirects:
    print("There were more redirects than what you allowed")
