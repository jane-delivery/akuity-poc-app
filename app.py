import logging
import sys
from flask import Flask, abort

# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')

app = Flask(__name__)

@app.route("/")
def root():
    return "hello"

@app.route("/400")
def error_400():
    abort(400)

@app.route("/500")
def error_500():
    abort(500)

@app.route("/hello")
def hello():
    return "world3"

if __name__ == "__main__":
    app.run(debug=True)

