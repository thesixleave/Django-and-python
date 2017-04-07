import sys
import json
import http.client, urllib.request,urllib.parse,urllib.error,base64

url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/14291855_1411718188845445_658205913628089434_n.jpg?oh=58f4f0b148f6b28ca6b75e7217229966&oe=59554DD1"

headers={
        'Content-Type':'application/json',
        'Ocp-Apim-Subscription-Key':'a752099ea5db4feea8146ceb1075c311',  
        }

body={'url':url}

params=urllib.parse.urlencode({
        'returnFaceId':'true',
        'returnFaceLandmarks':'false',
        'returnFaceAttributes':'age,gender,smile',
        
        })
try:
    conn =http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST","/face/v1.0/detect?%s"% params, json.dumps(body),headers)
    response=conn.getresponse()
    data = response.read()
    result=json.loads(data)
    print(json.dumps(result, indent=2, sort_keys=True))
    conn.close()
except Exception as e:
    print(e)