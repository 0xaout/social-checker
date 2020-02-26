import json

"""
on ouvre le fichier urls
"""
with open('urls.json', 'r') as f:
    data = json.loads(f.read())

while True:
    """
    on ajoute chaque entrée a la liste des urls ( CTRL-C pour sortir )
    """
    inputurl = input('url: ')
    data.append('https://' + inputurl + '/')

    with open('urls.json', 'w') as f:
        f.write(json.dumps(data, indent=4))