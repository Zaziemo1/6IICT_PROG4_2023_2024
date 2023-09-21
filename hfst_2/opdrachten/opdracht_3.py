import requests, json, time

url =  "https://restcountries.com/v3.1/all"
response = requests.get(url)
response_json = response.json()

landen = {}
for land in response_json:
    naam = land["name"]["common"]
    landen[naam] = land




            

 
