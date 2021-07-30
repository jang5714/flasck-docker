import unittest

from basic.one_to_ten_sum import One_to_ten


class One_to_ten_sum(unittest.TestCase):
     mock = One_to_ten()



     def test_one_to_ten_sum_3(self):
         self.mock.one_to_ten_sum_3()

if __name__ == '__main__' :
     unittest.main()
