from gtts import gTTS
import os

ttstext = input("What Do i have to say?             ")
languange = input("What language do i have to say it in?            ")



myobj = gTTS(text=ttstext, lang=languange, slow=False)
myobj.save('voice.mp3')
os.system('start voice.mp3')



