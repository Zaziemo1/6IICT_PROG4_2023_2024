fruit_lijst = ["Appel", "Banaan", "Kers"]
try:
    getal = input( "Geef een getal: " )
    if "." in getal:
        getal = float( getal )
    else:
        getal = int( getal )
    print( fruit_lijst[getal] )
except ValueError:
    print( "Er ging iets fout" ) 
except IndexError:
    print( "Er ging iets fout" ) 
except:
    print( "Er ging iets fout" ) 

print("Programma klaar") 