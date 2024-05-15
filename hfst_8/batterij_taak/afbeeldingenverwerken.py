import cv2
import os
from matplotlib import pyplot as plt

def plt_imshow(titel, afbeelding):
    plt.imshow(afbeelding, cmap='Greys_r')
    plt.title(titel)
    plt.grid(False)
    plt.show()

# Inladen alle bestanden in deze folder.
folder_pad    = r"hfst_8\batterij_taak\afbeeldingen"
folder_inhoud = os.listdir(folder_pad) 

# Overloop alle afbeeldingen in folder.
for index, bestand in enumerate(folder_inhoud):
    if (".png" in bestand) or (".jpeg" in bestand): # We werken enkel met png- of jpg-bestanden.
        print("hallo")
        # Inladen afbeelding
        bestand_pad    = f"{folder_pad}/{bestand}"
        naam, extensie = os.path.splitext(bestand)
        afbeelding     = cv2.imread(bestand_pad) 

        # Roteer afbeelding + opslaan.
        bestand_rotate = cv2.rotate(afbeelding, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite(filename=f'{folder_pad}/verwerkte/{naam}_rotate.{extensie}', img=bestand_rotate)
        # Spiegel afbeelding + opslaan.
        bestand_flip = cv2.flip(afbeelding, -1)
        cv2.imwrite(filename=f'{folder_pad}/verwerkte/{naam}_flip.{extensie}', img=bestand_flip)

        # Filter afbeelding (liefst wazig maken) + opslaan.
        bestand_blur = cv2.blur(afbeelding, (100,100))
        cv2.imwrite(filename=f'{folder_pad}/verwerkte/{naam}_blur.{extensie}', img=bestand_blur)



