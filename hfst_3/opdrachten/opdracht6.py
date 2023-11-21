import tkinter as tk
from pytube import YouTube

app= tk.Tk()

url = "https://www.youtube.com/watch?v=_NRn2W0Civc"
resolution = ["720p","380p"]
Label = tk.Label(master=app, text="Geef een youtube link op!")
Entry = tk.Entry(master=app, text=url)

yt = YouTube(url)
Menu = tk.Menu(master=app,text=f"Choose Resolution:{resolution}")



stream = yt.streams.filter(file_extension="mp4", progressive=True,).first()
Menu.pack()
Label.pack()
Entry.pack()



app.mainloop()
