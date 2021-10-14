import string
import random

import numpy as np
import pandas as pd
from icecream import ic


class MyPan(object):

    pd.DataFrame()
    pd.DataFrame



    def __init__(self):
        self.id = ["".join([random.choice(string.ascii_letters) for i in range(5)]) for i in range(10)]
        self.score = np.random.randint(0, 101, (10, 4))
        self.score2 = np.random.randint(0,100)
        self.student_columns = ['국어','영어','수학','사회','과학']
        self.animal_df = pd.read_csv('animal.csv', index_col=0)
        self.animal_df2 = pd.read_csv('animal1.csv', index_col=0)
        print('### PANDAS QUIZ ###')

    def quiz_1(self):
        my_dict = pd.DataFrame({"a": ['1', '2'], "b": ['3', '4'], "c": ['5', '6']}, index=['1', '2'])
        # DF = pd.DataFrame.from_dict({"1": [1,3,5], "2": [2,4,6]}, orient='index', columns=['a', 'b','c'])
        ic(my_dict)

        '''
        Q1. 다음 결과 출력
           a  b  c
        1  1  3  5
        2  2  4  6
        ic| df1:    a  b  c
                 1  1  3  5
                 2  2  4  6
        '''

    def quiz_2(self):
        my_dict = pd.DataFrame({"A": range(1,11,3), "B": range(2,12,3), "C": range(3,13,3)},
                               index=range(1,5))
        df = pd.DataFrame([[1,2,3],
                          [4,5,6],
                          [7,8,9],
                          [10,11,12]], index=range(1,5), columns=['A','B','C'])
        ic(df)


        '''         
        Q2. 다음 결과 출력
           A   B   C
        1   1   2   3
        2   4   5   6
        3   7   8   9
        4  10  11  12
        ic| df2:     A   B   C
                 1   1   2   3
                 2   4   5   6
                 3   7   8   9
                 4  10  11  12
        '''

    def quiz_3(self):
        # data3 = {'0': [random.randrange(11, 100),random.randrange(11, 100)], '1':[random.randrange(11, 100),random.randrange(11, 100)], '2': [random.randrange(11, 100),random.randrange(11, 100)]}
        df = pd.DataFrame(np.random.randint(11, 100, (2, 3)))
        ic(df)

        ''' 
        Q3 두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df3:     0   1   2
                 0  95  25  74
                 1  44  24  97
        '''

    def quiz_4(self):
        df = pd.DataFrame(self.score, columns=['국어', '영어', '수학', '사회'], index=self.id)
        ic(df)
        return df

        ''' 
        Q4 국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성. 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
        ic| self.id(): 'HKKHc'
        ic| self.score(): 22
        ic| df4:        국어  영어  수학  사회
               lDZid  57  90  55  24
               Rnvtg  12  66  43  11
               ljfJt  80  33  89  10
               ZJaje  31  28  37  34
               OnhcI  15  28  89  19
               claDN  69  41  66  74
               LYawb  65  16  13  20
               QDBCw  44  32   8  29
               PZOTP  94  78  79  96
               GOJKU  62  17  75  49
        '''

    def quiz_5(self):
        # print(self.quiz_4()['국어'])
        # df_by_other_method = pd.DataFrame({
        #     '국어': self.score,
        #     '영어': self.score,
        #     '수학': self.score,
        #     '사회': self.score
        #
        # }, index=[self.id])

        # for i in range(1, 10):
        #     df_by_other_method.loc[self.id] = {
        #         '국어': self.score,
        #         '영어': self.score,
        #         '수학': self.score,
        #         '사회': self.score
        #     }
        # ic(df_by_other_method)
        # df5 = pd.DataFrame([[]], index=[self.id])
        # df5 = [lambda x : df5.loc[self.id] for i in range(1,10)]
        # print(df5)
        # ic(df5)
        '''
        score = [np.random.randint(0,100) for i in range(1,5)]
        subject = ['국어','영어','영어','수학']
        dc = dict(zip(subject,score))
        student = "".join(random.choice(string.ascii_letters) for i in range(5))
        df10 = pd.DataFrame(dc, index=["".join(random.choice(string.ascii_letters) for i in range(5))])

        for i in range(1, 10):
            df5.loc["".join(random.choice(string.ascii_letters) for i in range(5))] = \
                dict(zip(subjects, list(map(lambda x: np.random.randint(0, 101), range(5)))))
        '''

        df5 = pd.DataFrame({zip(['국어','영어','영어','수학'],[np.random.randint(0,100) for i in range(1,5)])},
                           index=["".join([random.choice(string.ascii_letters) for i in range(5)]) for i in range(10)])
        # df6 = pd.DataFrame([[]] , index=[], columns=[])
        ls = [list(map())]
        print(df5)
        ic(df5)
        ''' 

        df = pd.DataFrame()
        name_list = []
        df['국어'] = 0
        df['영어'] = 0
        df['수학'] = 0
        df['사회'] = 0
        df['과학'] = 0
        
        df.loc['ckSVA'] = [93,44,14,94]
        df.loc['CAOot'] = [25, 54, 29, 10]
        df.loc['fZTCh'] = [82, 65, 31, 31]
        df.loc['mqZJJ'] = [51, 56, 56, 3]
        df.loc['BKlLt'] = [34, 32, 67, 48]
        df.loc['KKYUN'] = [85, 24, 16, 8]
        df.loc['WAjFK'] = [28, 80, 52,43]
        df.loc['yBVgG'] = [25, 94, 93, 54]
        df.loc['lGmwZ'] = [32, 50, 95, 1]
        df.loc['GQzmY'] = [26, 37, 80, 27]
            
        Q5 4번 문제를 loc 를 통해 동일하게 작성
        ic| df5:        국어  영어  수학  사회
                 ckSVA  93  44  14  94
                 CAOot  25  54  29  10
                 fZTCh  82  65  31  31
                 mqZJJ  51  56  56   3
                 BKlLt  34  32  67  48
                 KKYUN  85  24  16   8
                 WAjFK  28  80  52  43
                 yBVgG  58  94  93  54
                 lGmwZ  32  50  95   1
                 GQzmY  59  37  80  27
        '''

    def quiz_5_1(self):
        scores = [list(map(lambda x:np.random.randint(0, 101), [i for i in range(1, 5)])) for i in range(1, 11)]
        id = ["".join([random.choice(string.ascii_letters) for i in range(5)]) for i in range(10)]
        df2 = pd.DataFrame(scores, columns=['국어', '영어', '수학', '사회'], index=id)
        # df = pd.DataFrame(np.random.randint(0, 100, (10, 4)), columns=['국어', '영어', '수학', '사회'], index=id)
        # dfc = pd.read_csv('students5.csv', index_col=0)
        # dfc.drop(['Unnamed: 0'], axis = 1, inplace = True)
        ic(df2)
        ic(df2.loc[:,'국어'])
        # print(dfc['국어'])

        ''' 
        Q5-1 국어 점수만 출력
                             hVoGW    93
                             QkpKK    25
                             oDmky    82
                             qdTeX    51
                             XGzWk    34
                             PAwgj    85
                             vnTmB    28
                             wuxIm    58
                             AOQFG    32
                             jHChe    59
                             Name: 국어, dtype: int64
        '''

    def quiz_5_2(self):
        id = ["".join([random.choice(string.ascii_letters) for i in range(5)]) for i in range(10)]
        df = pd.DataFrame(np.random.randint(0, 100, (10, 5)), columns=['국어', '영어', '수학', '사회', '과학'], index=id)
        df.to_csv('students5.csv')
        return df

        ''' 
        Q5-2 1등 점수만 출력
        ic| TdQOI	15	42	59	67

        '''

    def quiz_5_3(self):
        df = pd.read_csv('students5.csv', index_col=0)
        df['총점'] = df.sum(axis=1)
        ic(df)
        df.to_csv('student7.csv')

        df.loc[:,'과학'] = pd.Series([], index=df.index)

        ''' 
        Q5-3 기존 학생들에게 과학과목과 점수를 랜덤으로 추가
        ic| df5:     국어  영어  수학  사회  과학
                 hVoGW  93  44  14  94  86
                 QkpKK  25  54  29  10   8
                 oDmky  82  65  31  31   2
                 qdTeX  51  56  56   3  13
                 XGzWk  34  32  67  48  23
                 PAwgj  85  24  16   8  22
                 vnTmB  28  80  52  43  48
                 wuxIm  58  94  93  54  83
                 AOQFG  32  50  95   1  52
                 jHChe  59  37  80  27  39
        '''

    def quiz_5_4(self):
        df = pd.read_csv('student7.csv', index_col=0)
        # df['총점'] = df.sum(axis=1)
        ls = [df['국어'].sum(), df['영어'].sum(), df['수학'].sum(), df['사회'].sum(), df['과학'].sum(), df['총점'].sum()]
        ic(ls)

        ''' 

        Q5-4 각 학생들의 점수의 총점을 표현하는 컬럼을 추가
        ic| df5:    국어  영어  수학  사회  과학   총점
                 hVoGW  93  44  14  94  86  331
                 QkpKK  25  54  29  10   8  126
                 oDmky  82  65  31  31   2  211
                 qdTeX  51  56  56   3  13  179
                 XGzWk  34  32  67  48  23  204
                 PAwgj  85  24  16   8  22  155
                 vnTmB  28  80  52  43  48  251
                 wuxIm  58  94  93  54  83  382
                 AOQFG  32  50  95   1  52  230
                 jHChe  59  37  80  27  39  242
        '''

    def quiz_5_5(self):
        df = pd.read_csv('student7.csv', index_col=0)
        df = df.loc[10] = [df['국어'].sum(), df['영어'].sum(), df['수학'].sum(), df['사회'].sum(), df['과학'].sum(),df['총점'].sum()]
        ic(df)



        ''' 
        ls5 = df5.sum().tolist()
        ic(ls5)
        
        Q5-5 각 학생들의 점수의 총합을 리스트로 출력
            ic| ls: [547, 536, 533, 319, 376, 2311]
        '''
    def quiz_5_6(self):
        df = pd.read_csv('student7.csv', index_col=0)
        # crime['검거'] = crime.loc[:, self.arrest_columns].sum(axis=1)
        df.loc['과목총점'] = [df['국어'].sum(), df['영어'].sum(), df['수학'].sum(), df['사회'].sum(), df['과학'].sum(),
                           df['총점'].sum()]
        # df['과목총점'] = df.loc[:, self.student_columns].sum(axis=1)
        df.to_csv('student8.csv')
        ic(df)
        ''' 
        df5.loc['과목총점'] = ls5
        
        Q5-6 각 학생들의 점수의 총합과 마지막 행은 과목총점 추가해서 출력
        ic| df5:  국어   영어   수학   사회   과학    총점
                 hVoGW   93   44   14   94   86   331
                 QkpKK   25   54   29   10    8   126
                 oDmky   82   65   31   31    2   211
                 qdTeX   51   56   56    3   13   179
                 XGzWk   34   32   67   48   23   204
                 PAwgj   85   24   16    8   22   155
                 vnTmB   28   80   52   43   48   251
                 wuxIm   58   94   93   54   83   382
                 AOQFG   32   50   95    1   52   230
                 jHChe   59   37   80   27   39   242
                 과목총점   547  536  533  319  376  2311
        '''
    def quiz_5_7(self):
        df = pd.read_csv('student8.csv', index_col=0)
        df2 = df.drop(['과목총점'])
        ic(df2)
        ''' 
        df5.drop('과목총점', inplace=True)
        ic(df5)
                     
        Q5-7 방금 추가한 과목총점 삭제
        ic| df5:  국어  영어  수학  사회  과학   총점
                 hVoGW  93  44  14  94  86  331
                 QkpKK  25  54  29  10   8  126
                 oDmky  82  65  31  31   2  211
                 qdTeX  51  56  56   3  13  179
                 XGzWk  34  32  67  48  23  204
                 PAwgj  85  24  16   8  22  155
                 vnTmB  28  80  52  43  48  251
                 wuxIm  58  94  93  54  83  382
                 AOQFG  32  50  95   1  52  230
                 jHChe  59  37  80  27  39  242
        '''
    def quiz_5_8(self):
        df = pd.read_csv('student8.csv', index_col=0)
        df2 = df.sort_values('총점', ascending=False)
        ic(df2)
        '''        
        df5.sort_values(by=['총점'], ascending=False, inplace=True)
        ic(df5)
        
        Q5-8 총점 열 기준 내림차순 정렬
                 wuxIm  58  94  93  54  83  382
                 hVoGW  93  44  14  94  86  331
                 vnTmB  28  80  52  43  48  251
                 jHChe  59  37  80  27  39  242
                 AOQFG  32  50  95   1  52  230
                 oDmky  82  65  31  31   2  211
                 XGzWk  34  32  67  48  23  204
                 qdTeX  51  56  56   3  13  179
                 PAwgj  85  24  16   8  22  155
                 QkpKK  25  54  29  10   8  126
        '''
    def quiz_6_1(self):
        df_col = {'animal' : ['cat', 'cat','snake','dog','dog','cat','snake','cat','dog','dog'],
                  'age': [2.5, 2.5,0.5,np.NaN,5.0,2.0,4.5,np.NaN,7.0,3.0],
                  'visits':[1,3,2,3,2,3,1,1,2,1],
                  'priority':['yes', 'yes','no','yes','no','no','no','yes','no','no']}
        df = pd.DataFrame(df_col, index=['a','b','c','d','e','f','g','h','i','j'])
        ic(df)
        ic(df.describe())
        df.to_csv('animal.csv')
        '''  
        Q6 주어진 값으로 DataFrame 객체 생성
        6-1 객체내부 정보를 출력
        ic| df6:   animal  age  visits priority
                 a    cat  2.5       1      yes
                 b    cat  3.0       3      yes
                 c  snake  0.5       2       no
                 d    dog  NaN       3      yes
                 e    dog  5.0       2       no
                 f    cat  2.0       3       no
                 g  snake  4.5       1       no
                 h    cat  NaN       1      yes
                 i    dog  7.0       2       no
                 j    dog  3.0       1       no
        ic| df6.describe():             age     visits
                            count  8.000000  10.000000
                            mean   3.437500   1.900000
                            std    2.007797   0.875595
                            min    0.500000   1.000000
                            25%    2.375000   1.000000
                            50%    3.000000   2.000000
                            75%    4.625000   2.750000
                            max    7.000000   3.000000
        '''
    def quiz_6_2(self):
        dfo = self.animal_df
        ic(dfo.iloc[:3])
        '''  
        6-2 객체 상위 3열까지 출력
        ic| df6.iloc[:3]:   animal  age  visits priority
                          a    cat  2.5       1      yes
                          b    cat  3.0       3      yes
                          c  snake  0.5       2       no
        '''
    def quiz_6_3(self):
        dfo = self.animal_df
        ic(dfo.loc[:, ['animal', 'age']])
        '''  
        6-3 animal과 age 컬럼만 출력
        ic| df6.loc[:, ['animal', 'age']]:   animal  age
                                           a    cat  2.5
                                           b    cat  3.0
                                           c  snake  0.5
                                           d    dog  NaN
                                           e    dog  5.0
                                           f    cat  2.0
                                           g  snake  4.5
                                           h    cat  NaN
                                           i    dog  7.0
                                           j    dog  3.0

        '''
    def quiz_6_4(self):
        dfo = self.animal_df
        ic(dfo.loc[dfo.index[[3,4,8]], ['animal','age']])
        '''                                                            
        6-4 객체의 3, 4, 8번 행에 해당하는 animal과 age 값만 출력
        ic| df6.loc[df6.index[[3,4,8]], ['animal','age']]:   animal  age
                                                           d    dog  NaN
                                                           e    dog  5.0
                                                           i    dog  7.0
        '''

    def quiz_6_5(self):
        dfo = self.animal_df
        ic(dfo[dfo['visits']>2])
        ''' 
        6-5 visit 컬럼에서 3 초과하는 값 출력
        ic| df6[df6['visits']>2]:   animal  age  visits priority
                                  b    cat  3.0       3      yes
                                  d    dog  NaN       3      yes
                                  f    cat  2.0       3       no
        '''

    def quiz_6_6(self):
        dfo = self.animal_df
        ic(dfo[dfo['age'].isnull()])
        ''' 
        6-6 age 에서 NaN 값 출력
        ic| df6[df6['age'].isnull()]:   animal  age  visits priority
                                      d    dog  NaN       3      yes
                                      h    cat  NaN       1      yes
        '''

    def quiz_6_7(self):
        dfo = self.animal_df
        ic(dfo[(dfo['age'] <3) & (dfo['animal'] =='cat')])
        '''         
        6-7 age가 3살 미만 고양이값 출력
        ic| df6[(df6['age'] <3) & (df6['animal'] =='cat')]:   animal  age  visits priority
                                                            a    cat  2.5       1      yes
                                                            f    cat  2.0       3       no
        '''

    def quiz_6_8(self):
        dfo = self.animal_df
        ic(dfo[dfo['age'].between(2,4)])
        '''        
        6-8 age가 2살이상 4살 미만인 값 출력
        ic| df6[df6['age'].between(2,4)]:   animal  age  visits priority
                                          a    cat  2.5       1      yes
                                          b    cat  3.0       3      yes
                                          f    cat  2.0       3       no
                                          j    dog  3.0       1       no
        '''
    def quiz_6_9(self):
        dfo = self.animal_df
        dfo['age'] = dfo['age'].replace([2.0],1.5)
        ic(dfo)
        '''
        df6.loc['f','age'] = 1.5
                              
        6-9 f 행의 나이를 1.5살로 변경
                 a    cat  2.5       1      yes
                 b    cat  3.0       3      yes
                 c  snake  0.5       2       no
                 d    dog  NaN       3      yes
                 e    dog  5.0       2       no
                 f    cat  1.5       3       no
                 g  snake  4.5       1       no
                 h    cat  NaN       1      yes
                 i    dog  7.0       2       no
                 j    dog  3.0       1       no
        '''
    def quiz_6_10(self):
        dfo = self.animal_df
        ic(dfo['visits'].sum())
        ''' 
        6-10 객체에서 visit 의 합 출력
        ic| df6['visits'].sum(): 19
        '''
    def quiz_6_11(self):
        dfo = self.animal_df
        ic(dfo.groupby('animal')['age'].mean())
        ''' 
        6-11 동물별로 나이의 평균 출력
        ic| df6.groupby('animal')['age'].mean(): animal
                                                 cat      2.333333
                                                 dog      5.000000
                                                 snake    2.500000
                                                 Name: age, dtype: float64
        '''
    def quiz_6_12(self):
        dfo = self.animal_df
        new_data = {'animal':'dog', 'age':'5.5', 'visits':'2', 'priority':'no'}
        dfo2 = dfo.append(new_data, ignore_index=True)
        ic(dfo2)
        return dfo2
        '''
        df6.loc['k'] = ['dog', 5.5,2,'no']
                
        6-12 k행을 추가하여 dog , 5.5세, 방문회수 2회, 우선권없음(no) 열을 추가
                 a    cat  2.5       1      yes
                 b    cat  3.0       3      yes
                 c  snake  0.5       2       no
                 d    dog  NaN       3      yes
                 e    dog  5.0       2       no
                 f    cat  1.5       3       no
                 g  snake  4.5       1       no
                 h    cat  NaN       1      yes
                 i    dog  7.0       2       no
                 j    dog  3.0       1       no
                 k    dog  5.5       2       no
        '''
    def quiz_6_13(self):
        dfo = self.quiz_6_12()
        df = dfo.drop(10)
        ic(df)
        '''
        df6.drop('k', inplace=True) # del df['k'] 도 같음
                 
        6-13 방금 추가한 열 삭제
        ic| df6:   animal  age  visits priority
                 a    cat  2.5       1      yes
                 b    cat  3.0       3      yes
                 c  snake  0.5       2       no
                 d    dog  NaN       3      yes
                 e    dog  5.0       2       no
                 f    cat  2.0       3       no
                 g  snake  4.5       1       no
                 h    cat  NaN       1      yes
                 i    dog  7.0       2       no
                 j    dog  3.0       1       no
        '''
    def quiz_6_14(self):
        dfo = self.animal_df
        ic(dfo['animal'].value_counts())
        '''  
        6-14 객체에 있는 동물의 종류의 수 출력
        ic| df6['animal'].value_counts(): dog      4
                                          cat      4
                                          snake    2
                                          Name: animal, dtype: int64
        '''
    def quiz_6_15(self):
        dfo = self.animal_df
        ic(dfo.sort_values(by=['age','visits'], ascending=[False, True]))
        '''                
        6-15 age 는 내림차순, visits 는 오름차순으로 정렬
        ic| df6.sort_values(by=['age','visits'], ascending=[False, True]):   animal  age  visits priority
                                                                           i    dog  7.0       2       no
                                                                           e    dog  5.0       2       no
                                                                           g  snake  4.5       1       no
                                                                           j    dog  3.0       1       no
                                                                           b    cat  3.0       3      yes
                                                                           a    cat  2.5       1      yes
                                                                           f    cat  2.0       3       no
                                                                           c  snake  0.5       2       no
                                                                           h    cat  NaN       1      yes
                                                                           d    dog  NaN       3      yes
        '''
    def quiz_6_16(self):
        dfo = self.animal_df
        dfo['priority'] = dfo['priority'].apply(lambda x : True if x == 'yes' else False)
        ic(dfo)
        '''  
        df6['priority'] = df6['priority'].map({'yes': True, 'no': False})
        
        6-16 priority 의 yes를 True, no 를 False  로 맵핑 후 출력
        ic| df6:   animal  age  visits  priority
                 a    cat  2.5       1      True
                 b    cat  3.0       3      True
                 c  snake  0.5       2     False
                 d    dog  NaN       3      True
                 e    dog  5.0       2     False
                 f    cat  2.0       3     False
                 g  snake  4.5       1     False
                 h    cat  NaN       1      True
                 i    dog  7.0       2     False
                 j    dog  3.0       1     False
        '''
    def quiz_6_17(self):
        dfo = self.animal_df
        dfo['animal'] = dfo['animal'].apply(lambda x : 'python' if x == 'snake' else x)
        dfo.to_csv('animal1.csv')
        ic(dfo)

        '''
        df6['animal'] = df6['animal'].replace('snake', 'python')
                        
        6-17 snake 를 python 으로 값을 변경
        ic| df6:    animal  age  visits  priority
                 a     cat  2.5       1      True
                 b     cat  3.0       3      True
                 c  python  0.5       2     False
                 d     dog  NaN       3      True
                 e     dog  5.0       2     False
                 f     cat  2.0       3     False
                 g  python  4.5       1     False
                 h     cat  NaN       1      True
                 i     dog  7.0       2     False
                 j     dog  3.0       1     False
        '''
    def quiz_6_18(self):
        dfo = self.animal_df2
        an = pd.pivot_table(dfo, index=['animal'], columns=['visits'])
        ic(an)
        '''
        df6 = df6.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')                  
        
        6-18 각각의 동물 유형과 방문 횟수에 대해, 평균나이 출력,
        즉,각 행은 animal 이고, 각 열은 visits 이며, 값은 평균연령
        (힌트, 피벗 테이블을 활용해야 함)
        ic| df6: visits    1    2    3
                 animal
                 cat     2.5  NaN  2.5
                 dog     3.0  6.0  NaN
                 python  4.5  0.5  NaN
        '''
    def quiz_7(self):
        df = pd.DataFrame({'A' : [1,2,3,4,4,4,5,6,7,7,7,1,2,3,4,5,6,7]}).drop_duplicates()
        ic(type(df['A']))
        ic(df)
        '''
        df7 = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5,6, 7, 7]})
        df7 = df7.drop_duplicates()
        ic(type(df7['A']))
        ic(df7)
            
        Q7. 키값 A와 중복된 값이 제거된 1,2,3,4,5,6,7 이 출력
        ic| type(df7['A']): <class 'pandas.core.series.Series'>
          ic| df7:    A
                   0  1
                   1  2
                   3  3
                   4  4
                   5  5
                   8  6
                   9  7
        '''

    def quiz_8(self):
        # df = pd.DataFrame()
        df8 = pd.DataFrame(np.random.random(size=(5, 3)))
        df8 = df8.sub(df8.mean(axis=1), axis=0)
        ic(df8)
        '''
        
            
        Q8. 행의 각 요소에서 행의 평균을 뺀 값을 출력하되 부분집합으로 가로출력
        ic| df8:           0         1         2
                 0 -0.095803 -0.151800  0.247603
                 1 -0.254548  0.229442  0.025106
                 2 -0.134566  0.409687 -0.275121
                 3  0.340665  0.224261 -0.564927
                 4  0.059283  0.010734 -0.070017
        '''
    def quiz_9(self):
        df9 = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
        ic(df9.sum().idxmax())
        '''
        idmax() : 데이터 프레임 내 값 가운데 최고값의 인덱스 위치 반환
                        
        Q9. 가장 작은 합계를 가진 숫자열의 열을 출력(최대값은 max)
        ic| df9.sum().idxmax(): 'b'
        '''

    def quiz_10(self):
        df10 = pd.DataFrame(np.random.randint(0, 2, size=(10, 3)))
        ic(df10)
        ic(len(df10) - df10.duplicated(keep=False).sum())
        ic(df10.drop_duplicates(keep=False))
        '''
            
        Q10. 중복된 값이 없는 유니크한 열의 카운트 출력(중복되지 않은 행은 몇 개..)
        ic| df10:    0  1  2
                  0  1  0  0
                  1  1  1  1
                  2  1  0  1
                  3  0  1  1
                  4  1  0  0
                  5  1  1  1
                  6  0  1  1
                  7  0  0  1
                  8  0  1  0
                  9  0  1  1
        ic| len(df10) - df10.duplicated(keep=False).sum():
            3
        ic| df10.drop_duplicates(keep=False):
                     0  1  2
                  2  1  0  1
                  7  0  0  1
                  8  0  1  0
        '''

    def quiz_11(self):
        nan = np.nan
        data = [[0.04, nan, nan, 0.25, nan, 0.43, 0.71, 0.51, nan, nan],
                [nan, nan, nan, 0.04, 0.76, nan, nan, 0.67, 0.76, 0.16],
                [nan, nan, 0.5, nan, 0.31, 0.4, nan, nan, 0.24, 0.01],
                [0.49, nan, nan, 0.62, 0.73, 0.26, 0.85, nan, nan, nan],
                [nan, nan, 0.41, nan, 0.05, nan, 0.61, nan, 0.48, 0.68]]
        columns = list('abcdefghij')
        df11 = pd.DataFrame(data, columns=columns)
        ic(type(df11.isnull()))
        df11 = (df11.isnull().cumsum(axis=1) == 3).idxmax(axis=1)
        ic(df11)

        '''  
        Q11. 체의 각 행에 대해 세번째 NaN 값이 들어 있는 열을 찾으시오. 일련의 열 레이블을 반환해야 합니다.
        nan = np.nan
        data = [[0.04, nan, nan, 0.25, nan, 0.43, 0.71, 0.51, nan, nan],
                [nan, nan, nan, 0.04, 0.76, nan, nan, 0.67, 0.76, 0.16],
                [nan, nan, 0.5, nan, 0.31, 0.4, nan, nan, 0.24, 0.01],
                [0.49, nan, nan, 0.62, 0.73, 0.26, 0.85, nan, nan, nan],
                [nan, nan, 0.41, nan, 0.05, nan, 0.61, nan, 0.48, 0.68]]
        columns = list('abcdefghij')
          ic| type(df11.isnull()): <class 'pandas.core.frame.DataFrame'>
          ic| df11: 0    e
                   1    c
                   2    d
                   3    h
                   4    d
                  dtype: object
        '''

    def quiz_12(self):
        df12 = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
                             'vals': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})
        ic(type(df12.groupby('grps')))
        ic(type(df12.groupby('grps')['vals']))
        df12 = df12.groupby('grps')['vals'].max()
        ic(df12)
        '''  
        Q12. grps 에서 a, b, c 별로 가장 큰 값
            df12 = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
                           'vals': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})
          ic| type(df12.groupby('grps')): <class 'pandas.core.groupby.generic.DataFrameGroupBy'>
          ic| type(df12.groupby('grps')['vals']): <class 'pandas.core.groupby.generic.SeriesGroupBy'>
          ic| df12: grps
                  a    345
                  b     57
                  c    235
                  Name: vals, dtype: int64
        '''

    def quiz_13(self):
        print('Q13. 다음 DF13 객체를 list 로 변환')
        df13 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        ls = df13.values.tolist()
        ic(type(ls))
        ic(df13.values.tolist())
        '''  
        Q13. 다음 DF13 객체를 list 로 변환
        df13 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        ic| type(ls): <class 'list'>
        ic| df13.values.tolist(): [[1, 4], [2, 5], [3, 6]]
        '''

    def quiz_14(self):
        print('Q14. 아래 결과로 출력되는 DF 객체 전환 코드작성')
        df14 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        ic(df14.to_dict())

        '''  
        Q14. 아래 결과로 출력되는 DF 객체 전환 코드작성
        ic| df14.to_dict(): {'A': {0: 1, 1: 2, 2: 3}, 'B': {0: 4, 1: 5, 2: 6}}
        '''
