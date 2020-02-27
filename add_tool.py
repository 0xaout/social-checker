import json

#

with open('urls.json', 'r') as f:
    data = json.loads(f.read())

while True:
    """
    we ask the user to enter an url
    """

    inputurl = input('url: ')

    """
    each input are added to the url list
    ( ctrl-c to leave )
    """

    data.append(f'https://{inputurl}/')

    with open('urls.json', 'w') as f:
        f.write(json.dumps(data, indent=4))