from flask import Flask, request, g
from flaskext.mongoobject import MongoObject
import settings
from json import dumps

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

@app.route("/delete", methods=["GET"])
def delete_task():
  id = request.args["id"]
  # XXX - Not scalable way to delete one task
  for task in Task.query.find():
    if task.id == id:
      task.remove()
      break
  return "Deleted: %s" % id

@app.route("/", methods=["GET"])
def list_tasks():
  selector = lambda task: (task.id, task.name, task.description)
  return dumps(map(selector, Task.query.find()))

@app.route("/search", methods=["GET", "POST"])
def search():
  selector = lambda task: (task.id, task.name, task.description)
  name = request.form["name"]
  return dumps(map(selector, Task.query.find({"name":name})))
