# -*- coding: utf-8 -*-

'''CSV   
'''

import csv

books = []

f=open('C:\jmoon\goodreads_choice_award_2016_CSV.csv','r')
csvReader = csv.reader(f)

print csvReader

for row in csvReader:
	books.append(row)

print "There are %d books in list" %(len(books))


for i in range(len(books)):
    print books[i]

f.close
