# Pas de URL aan zoals aangegeven in de verschillende niveau's.
import requests,json

grap = 1
joke = 0
# Bepaal of de grap uit 1 of 2 delen bestaat.


url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=political&amount=3"
response_json = requests.get(url).json() # Haal JSON uit response.

with open("hfst_2/oefenmee/JOKE.json", "w") as fp:
  json.dump(response_json, fp)

while joke <3:
  print(f"Grap {grap}: ")
  if ("joke" in response_json["jokes"][joke]):
    print(response_json["jokes"][joke]["joke"])     # De grap
    joke = joke+1
  else:
    print(response_json["jokes"][joke]["setup"])    # De setup
    print(response_json["jokes"][joke]["delivery"]) # De punchline
    joke= joke +1
  grap= grap+1


