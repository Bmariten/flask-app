from flask import Flask

app = Flask(__name__)

@app.route("/")
def start_page():
    return "Welcome to the start page"

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)