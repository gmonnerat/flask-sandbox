from flask import Flask, request
from flaskext.mongoobject import MongoObject
import settings

app = Flask(__name__)

app.config['MONGODB_HOST'] = settings.MONGODB_HOST
app.config['DEBUG'] = settings.DEBUG
app.config['MONGODB_DATABASE'] = settings.MONGODB_DATABASE_DEVELOPMENT

db = MongoObject(app)

class Task(db.Model):
  __collection__ = "tasks"


@app.route("/add", methods=["POST"])
def new_task():
  name = request.form["name"]
  description = request.form["description"]
  task = Task(name=name, description=description)
  task.save()
  return "Saved!"
