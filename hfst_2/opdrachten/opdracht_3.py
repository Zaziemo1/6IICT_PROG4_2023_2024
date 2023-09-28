import requests, json, time

url =  "https://restcountries.com/v3.1/all"
response = requests.get(url)
response_json = response.json()
name_landen = []
landen = {}

for land in response_json:
  
    naam = land["name"]["common"]
    name_landen.append(naam)
    landen[naam] = land

   

while True:
    gebr_land = str(input("Name a country:          "))

    if gebr_land in landen:
        print("Land bestaat")
        print(f"""\n{landen[gebr_land]['name']['common']}
Hoofdstad: {landen[gebr_land]['capital'][0]}.
Inwoners: {landen[gebr_land]['population']} inwoners.
Talen: {landen[gebr_land]['languages']}
Neighbours: {landen[gebr_land]['borders']}

""")
    elif gebr_land == "":
        break
    else:
        print("Land bestaat niet.")


            

 
