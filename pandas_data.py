##pandas 데이터 형태
# 참고 : http://yubylab.tistory.com/entry/Python-ch5-Pandas
# -*- coding: utf-8 -*-


def print_bar ():
    print '\n-------------------------------------------\n'


from pandas import Series, DataFrame
import pandas as pd



######### pandas 데이터 형태1 (Series) ########
seri1 = Series([4, -7, 5, 3])

# 라벨 설정
seri2 = Series([4,7,-5,3], index=['d','b', 'a', 'c'])


# 라벨 연산 하기
print_bar()
print 'seri2[\'a\'] : ', seri2['a']
print 'seri2[seri2>0] :\n', seri2[seri2>0]
print_bar()


# 딕셔너리에서 pandas 데이터 형태로
dic_data = {'Ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah' : 5000}
seri3 = Series(dic_data)
print 'dictionary to pandas :\n', seri3
print_bar()


# 인덱스 변경하기
states = ['California', 'Ohio', 'Oregon', 'Texas']
seri4 = Series(dic_data, index=states)
print 'dictionary to pandas (index modifying) :\n', seri4
print_bar()


'''
((**주의**))
print seri4['Utah']

(RESULT)
Traceback (most recent call last):
  File "series.py", line 29, in <module>
    print seri4['Utah']
  File "/usr/lib/python2.7/site-packages/pandas/core/series.py", line 601, in __getitem__
    result = self.index.get_value(self, key)
  File "/usr/lib/python2.7/site-packages/pandas/core/indexes/base.py", line 2491, in get_value
    raise e1
KeyError: 'Utah'
'''

print 'pd.isnull(seri4) :\n', pd.isnull(seri4)
#print 'pd.notnull(seri4) :\n', pd.notnull(seri4)
print_bar()

# 객체 이름, 인덱스 타이틀 설정하기
seri4.name = 'population'
seri4.index.name = 'state'
print 'giving name :\n', seri4
print_bar()





######### pandas 데이터 형태2 (DataFrame) ########

data = {'state' : ['Ohio', 'Ohio','Ohio', 'Nevada','Nevada'], 'year' : [2000, 2001, 2002, 2001, 2002], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame1 = DataFrame(data)
print 'frame1 :\n', frame1
print_bar()

# 칼럼 순서 바꾸기
frame2 = DataFrame(data, columns = ['year', 'state', 'pop'])
print 'change column order :\n', frame2
print_bar()

# 데이터 가로 추출
print 'print state :\n', frame2['state']
print_bar()

# 데이터 세로 추출
print 'print 3rd row :\n', frame2.ix[3]
print_bar()

