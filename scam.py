import requests
import os
import random
import string
import json

chars = string.ascii_letters + letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'http://localhost/MVC_projects/YaddaUC/index.php'

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@yahoo.com'
	password = ''.join(random.choice(chars) for i in range(8))

    requests.post(url, allow_redirects=False, data={
        'hello': username,
        "world": password
    })
