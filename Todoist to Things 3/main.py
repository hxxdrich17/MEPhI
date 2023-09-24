import requests
from email.mime.text import MIMEText
from email.header    import Header
import json
import time


api = "8edab8a380105ed826cacbf0e7eb0b7d62344310"
headers = {
            'Authorization': 'Bearer ' + api,
        }

arr = []

response = requests.get('https://api.todoist.com/rest/v2/tasks', headers=headers)
response.json()
synctask = json.loads(response.text)
tasks = json.loads(response.text)

for i in range(len(tasks)):
    arr.append(tasks[i].get("id"))
    
def send_email(arr):
    import smtplib
    user = "moskalenkoivan228@gmail.com"
    pwd = "apsyrduqrrzdiyrk"
    to = "add-to-things-mjxs3oi5cu1ls8ifd61@things.email"
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, pwd)
        for i in range(len(arr)):
            message = MIMEText(arr[i][1], 'plain', 'utf-8')
            message['Subject'] = Header(arr[i][0], 'utf-8')
            server.sendmail(user, to, message.as_string())
            time.sleep(1)
        server.close()
        return True
    except:
        print("EMAIL ERROR")
        return False
        

while (True):
    time.sleep(10)
    try:
        response = requests.get('https://api.todoist.com/rest/v2/tasks', headers=headers)
        response.json()
        synctask = json.loads(response.text)

        text = ""
        description = ""
        ans = []

        if (len(synctask) >= 1):
            for i in range(len(synctask)):
                if (synctask[i].get("id") not in arr):
                    text = synctask[i].get("content")
                    if (synctask[i].get("description") != ""):
                        description = synctask[i].get("description")
                if (text != ""):
                    ans.append([text, description])
                    text,description = "", ""
            send_email(ans)
        ans.clear()
        arr.clear()
        for i in range(len(synctask)):
            arr.append(synctask[i].get("id"))
    except:
        print("ERROR")
