import requests
import json

#

with open('urls.json', 'r') as f:
    data = json.loads(f.read())

"""
asking the user to enter the username he want to check
"""

username = input('username: ')

for n, i in enumerate(data):
    """
    for each url in the urls list we make a 
    request on the actual website to know if the
    username is free or not
    """

    r = requests.get(i + username)

    if r.status_code == 404:
        """
        if the status code is 404, it mean that the 
        page existe so the username is available
        """

        print('\u001b[32m' + data[n] + username + ' -> DISPONIBLE\033[0m', end='')

    else:
        """
        for every other status code, the username is not available
        """

        print('\u001b[31m' + data[n] + username + ' -> INDISPONIBLE\033[0m', end='')


