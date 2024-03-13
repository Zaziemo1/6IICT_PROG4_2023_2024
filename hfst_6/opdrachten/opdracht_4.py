# Bepaal recursief of een getal voldoet aan het luhn-criteria.
def luhn(reeks,teller=1):
    reeks = str(reeks)
    if len(reeks) == 1:
        return reeks
    
    cijfer = int(reeks[0])
    if (teller % 2) == 1:
        cijfer = 2*cijfer
    if cijfer > 9:
        cijfer = cijfer - 9

    totaal = cijfer + int(luhn(reeks[1:], teller+1))
    return totaal


print( luhn(4687612962034330) ) # 70 --> geldig
print( luhn(6728003096702784) ) # 70 --> geldig
print( luhn(2727903413621029) ) # 66 --> ongeldig
print( luhn(9727009535679498) ) # 92 --> ongeldig