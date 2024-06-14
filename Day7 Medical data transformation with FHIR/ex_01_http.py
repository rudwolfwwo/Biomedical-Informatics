import requests


#1.2 returns ('{"text":"!ollaH"}\n', 200)
def sendPOSTRequest(url, payload):
    x = requests.post(url,data=payload, headers={"Content-Type":"application/json"})
    return x.text,x.status_code

def sendGETRequest(url):
    x = requests.get(url)
    return x.text,x.status_code

def sendDELETERequest(url):
    x = requests.delete(url)
    return x.text,x.status_code