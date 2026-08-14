from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Tekst aangepast stap 6.</p>"