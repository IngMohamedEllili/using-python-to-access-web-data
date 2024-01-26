import urllib.parse, urllib.error, urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url='http://py4e-data.dr-chuck.net/json?'
adresse=input('tapez votre adresse')
html= url+ urllib.parse.urlencode({'address':adresse,'key':42})
print('Retrieving :',html)

data= urllib.request.urlopen(html).read()
print('Retrieved :',len(data))
js=json.loads(data)
print('place id :',js['results'][0]['place_id'])
