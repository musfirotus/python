'''Combine Data'''

# referensi : https://docs.python.org/3/howto/urllib2.html

import urllib.request, json

with urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts") as url:
    posts = json.loads(url.read().decode())

with urllib.request.urlopen("https://jsonplaceholder.typicode.com/users") as url:
    users = json.loads(url.read().decode())

# filter data 'users' dengan id yang sama dengan id dari parameter
def user(id):
    return list(filter(lambda a: a['id'] == id, users))[0]

for post in posts:
    # filter data posts yang idnya sesuai dengan data users
    post['user'] = user(post['userId'])
    # dirapikan tampilan saat dieksekusi
    print(json.dumps(post, indent=4))

# Code by Musfirotus