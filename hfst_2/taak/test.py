import requests,json
from PIL import Image

url ='https://api.deezer.com/search?q=artist:"Playboi Carti"'
r = requests.get(url)
fr = r.json()

with open("hfst_2/taak/test.json","w") as f:
    json.dump(fr,f)
    print("complete")
# filename = "https://e-cdns-images.dzcdn.net/images/artist/79146f056c0ec39873ed2acd06fe1cf4/500x500-000000-80-0-0.jpg"
# im = Image.open(requests.get(filename,stream=True).raw)  
  
# # This method will show image in any image viewer  
# im.show()  

