import unittest
from algorithm import find_avg

class TestSearch(unittest.TestCase):
  def setUp(self):
  	    self.array = [10, 5, 20, 30, 1, 4]

  def test_successful(self):
    self.assertEqual(find_avg(self.array, 15, 5), 1)



if __name__ == '__main__':
    unittest.main()