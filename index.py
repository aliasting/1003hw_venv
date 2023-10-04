from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.jinja.html")

@app.route("/forest")
def forest():
    return "<h1>forest.</h1>"

