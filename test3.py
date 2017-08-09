#Test for flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/bye")
def bye():
	return "Goodbye motherfucker!"

if __name__ == "__main__":
    app.run()