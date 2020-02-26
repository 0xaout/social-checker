import requests
import json


with open('urls.json', 'r') as f:
    data = json.loads(f.read())

username = input('username: ')

for n, i in enumerate(data):
    r = requests.get(i + username)
    print()

    progression = str(n + 1) + '/' + str(len(data))
    
    if r.status_code == 404:
        print('\u001b[32m' + data[n] + username + ' -> DISPONIBLE\033[0m', end='')
    else:
        print('\u001b[31m' + data[n] + username + ' -> INDISPONIBLE\033[0m', end='')


