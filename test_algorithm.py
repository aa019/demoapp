import unittest
from algorithm import find_max

class TestSearch(unittest.TestCase):
  def setUp(self):
  	    self.array = [10, 5, 20, 30, 1, 4]

  def test_successful(self):
    self.assertTrue(find_max(self.array, 15, 5))



if __name__ == '__main__':
    unittest.main()