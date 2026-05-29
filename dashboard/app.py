from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Xyth Dashboard Online"

app.run(debug=True)