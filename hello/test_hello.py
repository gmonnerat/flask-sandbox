import unittest
from hello import app

class HelloTestCase(unittest.TestCase):

  def setUp(self):
    self.client = app.test_client()

  def test_hello_world(self):
    data = self.client.get("/").data
    self.assertEquals(data,
                      "Hello World!",
                      data)

  def test_hello_random_name(self):
    data = self.client.get("/gabriel").data
    self.assertEquals(data,
                      "Hello Gabriel!",
                      data)

if __name__ == "__main__":
  unittest.main()
