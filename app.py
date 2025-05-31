from flask import Flask


app = Flask(__name__)


@app.route("/")

def home():

    return "Merhaba! Bu v1.0 sürümüdür."


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)

    