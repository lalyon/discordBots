#file for pulling dad jokes from icanhazdadjoke.com. They do not require API keys :)
import requests,json
headers = {
    'Accept': 'text/plain',
}

response = requests.get('https://icanhazdadjoke.com/', headers=headers)
print(response.text)
url = "https://icanhazdadjoke.com/"
req = requests.post(url)
#print (req.text)
#print (req.json) # maybe? 
