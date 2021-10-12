import unittest

from book_algorithm_interview.chap_02_program_language import OneToTenSum


class One_to_ten_sum(unittest.TestCase):
     mock = OneToTenSum()



     def test_one_to_ten_sum_3(self):
         self.mock.one_to_ten_sum_3()

if __name__ == '__main__' :
     unittest.main()
