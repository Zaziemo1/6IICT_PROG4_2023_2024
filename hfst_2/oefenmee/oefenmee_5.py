# Pas de URL aan zoals aangegeven in de verschillende niveau's.
import requests

grap = 0
joke = 0
# Bepaal of de grap uit 1 of 2 delen bestaat.
while joke < 3:
  grap= grap+1
  url = "https://v2.jokeapi.dev/joke/Christmas?amount=3?safe-mode"
  response_json = requests.get(url).json() # Haal JSON uit response.
  print(f"Grap {grap}: ")
  if ("joke" in response_json):
    print(response_json["joke"])     # De grap
    joke = joke+1
  else:
    print(response_json["setup"])    # De setup
    print(response_json["delivery"]) # De punchline
    joke= joke +1
    
