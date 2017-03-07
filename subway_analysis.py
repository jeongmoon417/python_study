# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import csv

def countRiding(rows_get):

    sum=0

    print 'print len', len(rows_get)

    riding = '승차'
    # utf-8 to euc-kr
    riding2 = unicode(riding, 'utf-8').encode('euc-kr')

    print riding2


    ###utf-8 to euc-kr????
    for i in range(len(rows_get)):
        if rows_get[i][2] == riding2:
            print rows_get[i][0] + '추가'
            for j in range(len(rows_get[i])-3):
                #ERROR : ValueError: invalid literal for int() with base 10: '2,111 '
                sum += int(rows_get[i][j+3])
        #else:
            #print 'rows_get[i][2] = ' + rows_get[i][2] + ' || str = ' + str(unicode(riding))


    return  sum


def main() :
    rows=[]

    f=open('riding_and_disembarking_passanger_201606.csv','r')
    csvReader=csv.reader(f)

    for row in csvReader:
        #rows.append(map(list_to_change, row))
        rows.append(row)

    f.close

    print "There are %d rows in list" %(len(rows))

    num_ride = countRiding(rows)
    #print 'print rows', rows
    print num_ride

if __name__ == "__main__" :
    main()