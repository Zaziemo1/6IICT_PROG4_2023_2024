# Gebruik onderstaande code om deze opdracht op te lossen.

# Pad naar het bestand (Plak in variabele het relatieve pad)
pad = "C:/Users/IFZA190706/OneDrive - MOSA-RT/6IICT/PROG_6IICT/github/6IICT_PROG4_2023_2024/hfst_1/opdrachten/opdracht_11_lied.txt"

# Open het tekstbestand met lied & zet inhoud van lied in string.
with open(pad, "r") as fp:
    lied = fp.read()

# Haal witregels weg uit string & zet string om naar lijst.
lied = lied.replace("/n","")
lied = lied.split()
gesoorterde_lied = {}
# Print lied (om te testen dat het werkt)

for lyric in lied:
    waarde = lied.count(lyric)
    if lyric in gesoorterde_lied:
        pass
    else:
        gesoorterde_lied[lyric] = waarde


    # print(f"{lyric} komt {waarde} voor")

sorted_lied = sorted(gesoorterde_lied.items(), key=lambda x:x[1], reverse=True)
for sort_lyric in sorted_lied:
    print(f"{sort_lyric[0]}: {sort_lyric[1]}")


