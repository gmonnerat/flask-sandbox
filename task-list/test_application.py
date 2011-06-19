import unittest
from application import app

class TaskListTestCase(unittest.TestCase):

  def test_add_task(self):
    client = app.test_client()
    response = client.post("/add", data={"name":"One Task",
                                   "description":"Do Something"})
    self.assertEquals(response.status_code, 200, response.status_code)


if __name__ == "__main__":
  unittest.main()
