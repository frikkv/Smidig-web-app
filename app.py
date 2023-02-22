from flask import Flask, render_template
from api import*

bilder = hent_bilder(iden)
ider = hent_id()
tittel = hent_tittel(iden)
forsok = 0 

app = Flask(__name__)


def sjekk_svar():
    if gjett != tittel: 
        neste_runde()
    else: 
        print("Riktig")

@app.route("/")
def index():
    navn = "Api"
    return render_template("index.html", navn=navn, ider=ider, tittel=tittel)

def rute_seier():
    return render_template("seier.html")
    
@app.route("/spill")
def rute_spill():
    global forsok,tittel
    return render_template("spill.html", ider=ider,bilder=alle_bilder[forsok],tittel=tittel)   

@app.route("/gjett",methods=["POST"])
def rute_gjett():
    global forsok
    forsok += 1
    gjett = requests.form["gjett"]
    if gjett == tittel:
        return rute_seier()
    else:
        return rute_spill()
  

