import unittest

from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1,2,3,4]
        result = sum(data)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
