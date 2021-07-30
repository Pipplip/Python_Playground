'''
Web-Requests

Anforderung:
pip install requests
'''
import requests

# print(help(r)) # Hilfe zu den responses


# get request, benutze post fuer post requests
# in rGet steht dann das Response Ergebnis
rGet = requests.get('https://www.google.com')
post_payload = {'username':'User1', 'password':'pass1'}
rPost = requests.get('https://httpbin.org/post', data=post_payload)

r_dict = rPost.json()
print(r_dict['form'])

print(rGet.text) # gibt html zurueck
print(rGet.status_code) # status code
print(rGet.headers) # response headers


# httpbin - Tool fuer http tests
get_payload = {'page':2, 'count':25}
r2 = requests.get('https://httpbin.org/get', params=get_payload)
print(r2.text)
print(r2.url)

'''
Auth
'''
rAuth = requests.get('https://httpbin.org/basic-auth/user1/pass1', auth=('user1','pass1'))
print(rAuth)
print(rAuth.text)

'''
Bilder herunterladen
'''
rPic = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Firefox_logo%2C_2019.svg/1200px-Firefox_logo%2C_2019.svg.png')

with open('meinBild.png', 'wb') as f:
    f.write(rPic.content)


