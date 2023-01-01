from flask import Flask, render_template, url_for
import webscraper

app = Flask(__name__)


@app.route('/')
def index():
    url_for('static', filename="style.css")
    return render_template("index.html")


app.run(host='0.0.0.0', port=81)
