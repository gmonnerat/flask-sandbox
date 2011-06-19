import unittest
from application import app
from json import loads

class TaskListTestCase(unittest.TestCase):

  def setUp(self):
    self.client = app.test_client()

  def tearDown(self):
    response = self.client.get("/")
    data = loads(response.data)
    for id, name, description in data:
      response = self.client.get("/delete?id=%s" % id)

  def test_add_task(self):
    response = self.client.post("/add", data={"name":"One Task",
                                   "description":"Do Something"})
    self.assertEquals(response.status_code, 200, response.status_code)

  def test_delete_task(self):
    self.client.post("/add", data={"name":"fix bug",
                                   "description":"Fix Bug"})
    response = self.client.post("/search", data=dict(name="fix bug"))
    data = loads(response.data)
    for id, name, description in data:
      response = self.client.get("/delete?id=%s" % id)
      self.assertEquals(200, response.status_code)

  def test_list_tasks(self):
    response = self.client.get("/")
    data = loads(response.data)
    self.assertEquals(data, [], data)

  def test_find_one_task(self):
    self.client.post("/add", data={"name":"fix something",
                                   "description":"Fix Something"})
    response = self.client.post("/search", data=dict(name="fix something"))
    data = loads(response.data)
    self.assertEquals(1, len(data))


if __name__ == "__main__":
  unittest.main()
