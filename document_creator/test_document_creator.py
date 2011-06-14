import unittest
from application import app

class DocumentCreatorTestCase(unittest.TestCase):

  def setUp(self):
    self.client = app.test_client()

  def test_add_image(self):
    res = self.client.post("/add",
                           data=dict(url="./data/image.png"))
    self.assertEquals(res.status_code, 200, res.data)

if __name__ == "__main__":
  unittest.main()
