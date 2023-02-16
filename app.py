from flask import Flask, render_template
from api import*

bilder = hent_bilder(iden)
ider = hent_id()
tittel = hent_tittel(iden)
gjett = input("Hva heter filmen?")
forsøk = 0 





app = Flask(__name__)


def sjekk_svar():
    if gjett != tittel: 
        neste_runde()
    else: 
        print("Riktig")


Oppgavenummer = 1
def neste_runde():
    Oppgavenummer+=1
    if Oppgavenummer == 1:
        return En()

    return En()
    #@app.route("/"+str(Oppgavenummer))

@app.route("/")
def index():
    navn = "Api"
    return render_template("index.html", navn=navn, ider=ider, bilde=alle_bilder[forsøk],tittel=tittel)



def rute_seier():
    return render_template("seier.html")
    
@app.route("/spill")
def rute_spill():
    global forsøk,tittel
    return render_template("spill.html", ider=ider,bilder=alle_bilder[forsøk],tittel=tittel)   

@app.route("/gjett",methods=["POST"])
def rute_gjett():
    forsøk += 1
    gjett = requests.form["gjett"]
    if gjett == tittel:
        return rute_seier()
    else:
        return rute_spill()
  

