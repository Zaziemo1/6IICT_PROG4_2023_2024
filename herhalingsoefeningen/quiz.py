import requests, json, random

def trivia_quiz():
    link = "https://opentdb.com/api.php?amount=1&category=22"
    response = requests.get(link) # GET de info van deze website.
    data = json.loads(response.text) # Haal tekst uit de info & zet om naar json.
    


    while True:
        link = "https://opentdb.com/api.php?amount=1&category=22"
        response = requests.get(link) # GET de info van deze website.
        data = json.loads(response.text) # Haal tekst uit de info & zet om naar json.
        vraag   =   data["results"][0]["question"]             # Haal de vraag uit de data (string).
        opties  =   data["results"][0]["incorrect_answers"]    # Haal incorrecte antwoorden uit de data (lijst van strings).
        correct =   data["results"][0]["correct_answer"]       # Haal correct antwoord uit de data (string).
        opties.insert(random.randrange(0, len(opties)), correct) # Zet correct antwoord op random positie in lijst opties.
        print(vraag)
        print(opties)
        antwoord = input("Selecteer een antwoord: ")
        if antwoord == "STOP":
            break
        if antwoord == correct:
            print("Correct!")
        else:
            print(f"Wrong, the correct answer is {correct}")

trivia_quiz()
    
