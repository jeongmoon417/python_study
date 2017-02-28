# -*- coding: utf-8 -*-

#데이터 분석 : CVS파일로 책제목 리스트 입력 -> 데이터 조작 -> 그래프 출력#

import csv
import re
import collections

import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
fuction : printlist
prints prints[*][index]
argument : prints(list to print) / index (index to print)
"""
def printlist (prints, index):
    print '\n'
    for i in range(len(prints)):
        print '*', i + 1, '. ', prints[i][index]

#CVS파일에서 책들을 리스트(books)에 저장#
books = []
f=open('goodreads_choice_award_2016_CSV.csv','r')
csvReader = csv.reader(f)
for row in csvReader:
	books.append(row)
f.close

#리스트 books 출력#
print "There are %d books in list" %(len(books))
print 'Books are..'
printlist(books,0)


# 대문자 -> 소문자 변환#
for i in range (len(books)):
    books[i].append(books[i][0].lower())
printlist(books,1)


#특수문자 제거#
for i in range (len(books)):
    books[i].append(re.sub("[!.%?:~-]", " ", books[i][1]))
printlist(books,2)

#알파벳 점유를 센다 -> 딕셔너리인 count에 저장#
book_text = []
for i in range (len(books)):
    book_text += books[i][2]
count = collections.Counter(book_text)
print count

'''
#알파벳을 입력 받아 해당 알파벳의 점유를 출력#
while(True):
    alp = raw_input('Enter any alphabet: ')
    if (len(alp) == 1):
        break
small_alp = alp.lower()
print 'The number of alphabet', small_alp, ':', count[small_alp]
'''

#그래프 그리기#
import numpy as np
import matplotlib.pyplot as plt
import string

plt.switch_backend('agg')

fig = plt.figure()

#딕셔너리 -> 리스트로 변환 후 막데 그래프로 그림#
alphabets = []  #empty list
alpha = list(string.ascii_lowercase)
big_alpha = list(string.ascii_uppercase)
for i in range(len(alpha)): #0-25
    tmplist = [alpha[i]]
    alphabets.append(tmplist)
alphabets2 = list(string.ascii_lowercase)
for i in range(len(alphabets)):
    alphabets[i].append(count[alphabets[i][0]])
print 'dictionary to list: ', alphabets

num_alpha=[]
for i in range(len(alpha)):
    num_alpha.append(count[alpha[i]])

print 'num_alpha', num_alpha

plt.bar(range(len(alpha)), num_alpha, facecolor='#f58282', edgecolor='white')

#add labels, title, axes ticks
plt.xticks(range(len(alpha)), big_alpha)
plt.title('Alphabetic occupation')


fig.savefig('book_data_analysis.png')


'''
#dictionary 바로 출력하기#
fig2 = plt.figure()
bar_x2=range(len(count))
plt.bar(bar_x2, count.values(), align='center', width=0.5)
plt.xticks(bar_x2, count.keys())
fig2.savefig('book_data_analysis2.png')
'''
