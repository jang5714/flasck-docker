
from book_algorithm_interview.chap_06_string.models import Palindrome
from book_algorithm_interview.chap_06_string.models import Reverse_String

if __name__ == '__main__':
    rever = Reverse_String()
    ls = rever.str_to_list("Input")
    resversed_ls = rever.reverse_str_list(ls)
    print(rever.list_to_str(resversed_ls))