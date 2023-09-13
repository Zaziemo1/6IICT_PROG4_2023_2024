import random
alfabet = "abcdefghijklmnopqrstuvwxyz"
cijfers = "0123456789"
groot_alfabet = alfabet.upper()
speciale_karakters = "@&#!|*%"



def password_generator(amount,include_alphabet,include_cijfers,include_upper,include_special):
    keuze = ""
    password = ""
    if include_alphabet == True:
           keuze += alfabet
    if include_cijfers == True:
           keuze += cijfers
    if include_upper == True:
           keuze += groot_alfabet
    if include_special == True:
           keuze += speciale_karakters
    while True:
        password = ""
        for i in range(amount):
            password += random.choice(keuze)
        if any(letter in password for letter in alfabet) or not include_alphabet:
            if any( cijfer in password for cijfer in cijfers) or not include_cijfers:
                  if any(gletter in password for gletter in groot_alfabet) or not include_upper :
                    if any( skarak in password for skarak in speciale_karakters) or not include_special:
                         break

    
    return password

print(password_generator(7,True,True,True,False))