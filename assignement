import urllib.parse , urllib.request, urllib.error
import json

url = "http://py4e-data.dr-chuck.net/comments_972290.json"
html = urllib.request.urlopen(url).read()

data = json.loads(html)
a=0
print(len(data))
for i in data["comments"]:
    a+=(int(i['count']))
print(a)
