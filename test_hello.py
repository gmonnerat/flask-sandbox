import unittest
from hello import app

class HelloTestCase(unittest.TestCase):

  def setUp(self):
    self.client = app.test_client()

  def testHelloWorld(self):
    data = self.client.get("/").data
    self.assertEquals(data,
                      "Hello World!",
                      data)

  def testHelloRandomName(self):
    data = self.client.get("/").data
    self.assertEquals(data,
                      "Hello Gabriel!",
                      data)

if __name__ == "__main__":
  unittest.main()
