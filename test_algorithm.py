import unittest
from algorithm import find_diff

class TestSearch(unittest.TestCase):
  def setUp(self):
  	    self.array = [10, 5, 20, 30, 1, 4]

  def test_successful(self):
    self.assertEqual(find_diff(self.array, 15, 5), 1)

  def test_successful2(self):
  	self.assertEqual(find_diff(self.array, 5, 15), 1)

  def test_failed(self):
  	self.assertNotEqual(find_diff(self.array, 3, 5), 1)

  def test_failed2(self):
  	self.assertNotEqual(find_diff(self.array, 15, 5), 0)

  def tes_failed3(self):
  	self.assertNotEqual(find_diff(self.array, 4, 3), 0)



if __name__ == '__main__':
    unittest.main()