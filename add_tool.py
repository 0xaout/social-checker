import json

#

with open('urls.json', 'r') as f:
    data = json.loads(f.read())

while True:
    """
    we ask the user to enter an url
    """

    url_input = input('url: ')

    """
    each input are added to the url list
    ( ctrl-c to leave )
    """

    if url_input[0:4] == 'http':
        data.append(f'{url_input}/')
    else: 
        data.append(f'https://{url_input}/')

    with open('urls.json', 'w') as f:
        f.write(json.dumps(data, indent=4))