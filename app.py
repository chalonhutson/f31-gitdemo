from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Best app ever made!!!!"


if __name__ == "__main__":
    app.run()