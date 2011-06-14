from flask import Flask
app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add_image():
  return "function called"
