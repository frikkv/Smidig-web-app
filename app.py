from flask import Flask, render_template
from api import*

app = Flask(__name__)


@app.route("/")
def index():
    navn = "Api"
    bilder = hent_bilder(iden)
    ider = hent_id()
    tittel = hent_tittel(iden)

    return render_template("index.html", navn=navn, ider=ider, bilder=bilder,tittel=tittel)

