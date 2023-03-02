import requests
from random import randint


url = "https://imdb-api.com/en/API/Top250Movies/k_yfwl9e9x"
resultat = requests.get(url, headers= {"User-Agent": "Frikk"})
data = resultat.json()


alle_titler = []
nmr = 0


def hent_alle_titler():
    global nmr
    for i in range(0,250):
        tittel = data["items"][nmr]["title"]
        alle_titler.append(tittel)
        nmr += 1
    return(alle_titler)


def hent_id():
    random_film = randint(0,250)
    id = data["items"][random_film]["id"]
    return id



def hent_bilder(iden):
    url = f"https://imdb-api.com/en/API/Images/k_yfwl9e9x/{iden}"
    resultat = requests.get(url, headers= {"User-Agent": "Frikk"})
    data = resultat.json()
    alle_bilder = []
    nmr = 0 
    for i in range(0,5):    
        bilder = data["items"][nmr]["image"]
        alle_bilder.append(bilder)
        nmr +=1
    return(alle_bilder)


        

def hent_tittel(iden):
    url = f"https://imdb-api.com/en/API/Images/k_yfwl9e9x/{iden}"
    resultat = requests.get(url, headers= {"User-Agent": "Frikk"})
    data = resultat.json()
    tittel = data["title"]
    return(tittel)








iden = hent_id()
hent_bilder(iden)
hent_tittel(iden)
hent_alle_titler()



