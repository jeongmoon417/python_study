"""
data analysis example
1. get data from csv file
2. process data (capital letters, special chracters)
3. count the number of alphabets
"""

import csv
import re
import collections

"""
fuction : printlist
prints prints[*][index]
argument : prints(list to print) / index (index to print)
"""
def printlist (prints, index):
    print '\n'
    for i in range(len(prints)):
        print '*', i + 1, '. ', prints[i][index]


books = []
f=open('goodreads_choice_award_2016_CSV.csv','r')
csvReader = csv.reader(f)
for row in csvReader:
	books.append(row)

f.close

#print the number of books, list of books
print "There are %d books in list" %(len(books))
print 'Books are..'
printlist(books,0)


# capital letters to small letters
for i in range (len(books)):
    books[i].append(books[i][0].lower())
printlist(books,1)


#delete special characters
for i in range (len(books)):
    books[i].append(re.sub("[!.%?:~-]", " ", books[i][1]))
printlist(books,2)

#counts alphabet
book_text = []
for i in range (len(books)):
    book_text += books[i][2]
count = collections.Counter(book_text)
print count

#get input
while(True):
    alp = raw_input('Enter any alphabet: ')
    if (len(alp) == 1):
        break
small_alp = alp.lower()
print 'The number of alphabet', small_alp, ':', count[small_alp]
