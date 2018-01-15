#using developer API key provided by giphy to send gifs via chat
import urllib,json
import urllib.request

data = json.loads(urllib.request.urlopen("http://api.giphy.com/v1/stickers/random?api_key=XK8ZzuTAvApm4OdLNDlQJsjCLbS44giv=&limit=5").read())
print (json.dumps(data, sort_keys=True, indent=4))
