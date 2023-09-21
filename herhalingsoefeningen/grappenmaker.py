import requests, json

def grappenmakker2000():
 link = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=political"
 response = requests.get(link)
 data = json.loads(response.text)
 
 grap = data["setup"]
 antwoord = data["delivery"]
 
 print(grap)
 print(antwoord)


 





grappenmakker2000()