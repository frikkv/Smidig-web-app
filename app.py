from flask import Flask, render_template
from api import hent_id

app = Flask(__name__)
id = hent_id()


@app.route("/")
def index():
    navn = "Api"
    return render_template("index.html", navn=navn, id=id)

