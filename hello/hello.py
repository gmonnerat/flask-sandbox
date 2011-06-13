from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/<username>")
def hello(username="World"):
  return "Hello %s!" % username.capitalize()

if __name__ == "__main__":
  app.run()
