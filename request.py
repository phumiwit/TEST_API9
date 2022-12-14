import requests
url = "http://localhost:5000/predict"
files = {'file':open('DEE.wav','rb')}
headers = {'content-type': 'audio/wav'}

resp = requests.post(url=url,files=files,headers=headers)

print(resp.json())