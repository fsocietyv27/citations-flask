import json
import random
from pathlib import Path
from flask import Flask, render_template, jsonify

BASE_DIR = Path(__file__).resolve().parent

# Charge les citations au démarrage
with open(BASE_DIR / "quotes.json", encoding="utf-8") as f:
    QUOTES = json.load(f)

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quote")
def quote():
    return jsonify({"citation": random.choice(QUOTES)})

if __name__ == "__main__":
    # debug=True pour rechargement auto pendant le dev
    app.run(host="0.0.0.0", port=5000, debug=True)