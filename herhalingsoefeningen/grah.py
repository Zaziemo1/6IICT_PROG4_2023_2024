import requests,json

API = "https://api.openai.com/v1/chat/completions"

response = requests.get(API)
data = json.loads(response.text)

print(data)