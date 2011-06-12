import unittest
from hello import app

class HelloTestCase(unittest.TestCase):

  def testHelloWorld(self):
    client = app.test_client()
    assert client.get("/").data == "Hello World!"

if __name__ == "__main__":
  unittest.main()
