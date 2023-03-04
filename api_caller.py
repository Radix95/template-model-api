# example of python client
# first performs a login, then it calls a protected API


import requests


response = requests.post('http://localhost:8000/login', data = {'username':'string', 'password':'string'})

auth = False

if response.status_code == 200:
    access_token = response.json()["access_token"]
    auth = True
else:
    print(response.json()["detail"])
    
if auth:

    my_headers = {'Authorization' : f'Bearer {access_token}'}

    response = requests.get('http://localhost:8000/modelml', headers=my_headers)

    if response.status_code == 200:
        resources = response.json()
        body = resources["data"]
        print(body)



