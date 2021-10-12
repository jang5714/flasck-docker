import string

import pandas as pd
from icecream import ic

class Conversion(object):
    def __init__(self):
        print('자료구조 타입변환 예제')
        print('Q1. 1부터 9까지 요소를 갖는 튜플 생성')
        tpl = self.create_tuple()
        ic(type(tpl))
        ic(tpl)
        print('Q2. 튜플을 리스트로 전환')
        lst = self.tuple_to_list(tpl)
        ic(type(lst))
        ic(lst)
        print('Q3. 리스트의 int 값을 float 로 전환')
        lst = self.int_to_float(lst)
        ic(type(lst))
        ic(lst)
        print('Q4. float 리스트를 int 리스트 로 전환')
        lst = self.float_to_int(lst)
        ic(type(lst))
        ic(lst)
        print('Q5. int 리스트를 딕셔너리로 전환. 단 키값은 int 를 str 로 변환시켜서 활용함')
        dic = self.list_to_dictionary(lst)
        ic(type(dic))
        ic(dic)
        print('Q6. "hello"를 가진 튜플생성')
        tpl = self.hello_to_tuple('hello')
        ic(type(tpl))
        ic(tpl)
        print('Q7. 6번 튜플을 리스트로 전환')
        lst = self.hello_to_list(tpl)
        ic(type(lst))
        ic(lst)
        print('Q8. 5번 딕셔너리를 dataframe 으로 전환')
        df = self.dictionary_to_dataframe(dic)
        ic(type(df))
        ic(df)

    def create_tuple(self) -> ():
        tpl = tuple(range(1,10))
        return tpl

    def tuple_to_list(self, tpl) -> []:
        lst = list(tpl)
        return lst

    def int_to_float(self, lst) -> []:
        # lst = list(map(float, lst))
        lst = [float(x) for x in lst]
        return lst

    def float_to_int(self, lst) -> []:
        # lst = list(map(int, lst))
        lst = [int(x) for x in lst]
        return lst

    def list_to_dictionary(self,lst) -> {}:
        # dictionary = dict.fromkeys([str(x) for x in lst],[i for i in range(9)])
        return {str(i): i for i in lst}

    def hello_to_tuple(self, str:str) -> ():
        tpl = tuple(str)
        return tpl

    def hello_to_list(self, tpl) -> []:
        lst = list(tpl)
        return lst

    def dictionary_to_dataframe(self, dic) -> object:
        df = pd.DataFrame.from_dict(dic, orient='index')
        return df

if __name__ == '__main__':
    Conversion()