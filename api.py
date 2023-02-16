import requests
from random import randint


url = "https://imdb-api.com/en/API/Top250Movies/k_yfwl9e9x"
resultat = requests.get(url, headers= {"User-Agent": "Frikk"})
data = resultat.json()

alle_titler = []
nmr = 0
for i in range(0,250):
    tittel = data["items"][nmr]["title"]
    alle_titler.append(tittel)
    nmr += 1
#print(alle_titler)


def hent_id():
    random_film = randint(0,250)
    id = data["items"][random_film]["id"]
    return id

def hent_bilder(iden):
    url = f"https://imdb-api.com/en/API/Images/k_yfwl9e9x/{iden}"
    resultat = requests.get(url, headers= {"User-Agent": "Frikk"})
    data = resultat.json()
    nmr = 0 
    alle_bilder = []
    for i in data:    
        bilder = data["items"][nmr]["image"]
        alle_bilder.append(bilder)
        nmr +=1
         print(alle_bilder)
        

def hent_tittel(iden):
    url = f"https://imdb-api.com/en/API/Images/k_yfwl9e9x/{iden}"
    resultat = requests.get(url, headers= {"User-Agent": "Frikk"})
    data = resultat.json()
    tittel = data["title"]
    return(tittel)

def display():
    for bilder in 



iden = hent_id()
hent_bilder(iden)
hent_tittel(iden)




