from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Best app ever made!!!!"

@app.route("/see-sky")
def see_sky():
    return "It is blue!!!!"


if __name__ == "__main__":
    app.run()