import json
import requests
from PIL import Image
geschiedenis = []
while True:
    keuze = int(input("""What do you want to search:
        1-Album
        2-Artist
        3-Track
        4-Stop 
                """))

    if keuze == 1:
        album = str(input("Name an album:   "))
        url = f'https://api.deezer.com/search?q=album:"{album}"'
        response = requests.get(url)
        response_json = response.json()
        counter = 0
        print(
            f"This album has been made by {response_json['data'][0]['artist']['name']}")
        while True:
          counter = int(counter)
          print(response_json['data'][counter]['title'])
          counter = counter+1
          if counter >= len(response_json["data"]):
               break
        keuze2 = input(
          f"Would you like to see more of {response_json['data'][0]['artist']['name']}?    ")
        if keuze2.upper() == 'YES':

          url2 = f"https://api.deezer.com/artist/{response_json['data'][0]['artist']['id']}/albums"
          response = requests.get(url2)
          response_json = response.json()
          counter2 = 0
          album = 1
          while True:
            print(f"Album {album}: {response_json['data'][counter2]['title']}")
            counter2 = counter2+1
            album = album+1
            if counter2 >= len(response_json["data"]):
               break

    if keuze == 2:
        artist = str(input("Name the artist who made it:    "))
        url = f'https://api.deezer.com/search?q=artist:"{artist}"'
        response = requests.get(url)
        response_json = response.json()
        print(f"""The most recent track: {response_json['data'][0]['title']}, its ranked {response_json['data'][0]['rank']} and its duration is {response_json['data'][0]['duration']}.
            The most recent album: {response_json['data'][0]['album']['title']},""")
        keuze3 = input("Do you want to see the artist?  ")
        if keuze3.upper() == 'YES':
            image = response_json['data'][0]['artist']['picture_big']
            im = Image.open(requests.get(image, stream=True).raw)  
            im.show()  

    if keuze == 3:
        track = str(input("Name the track you want to seach:      ")).upper()
        artist = str(input("Which artist made the song:     ")).upper()
        url = f'https://api.deezer.com/search?q=track:"{track}"'
        response = requests.get(url)
        response_json = response.json()

        counter2 = 0
        while True:
            counter2 = int(counter2)

            if artist == response_json['data'][counter2]['artist']['name'].upper():
                print(f"Made by {response_json['data'][counter2]['artist']['name']},{response_json['data'][counter2]['title']}. Its duration is {response_json['data'][counter2]['duration']}s and its ranked {response_json['data'][counter2]['rank']}")
                if response_json['data'][counter2]['explicit_lyrics'] == True:
                    print("This track contains explicit lyrics!")
                else:
                    print("This track doesnt contain explicit lyrics!")
                break

            counter2 = counter2 + 1
    if keuze == 4:
        print("Goodbye!")
        break
    else:
        print("Please type a number between 1 and 4! ")
