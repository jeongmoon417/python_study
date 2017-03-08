# -*- coding: utf-8 -*-

import sys
import re
import csv
import operator
import numpy

reload(sys)
sys.setdefaultencoding('utf-8')

def compareStr(st1, st2):
    if st2=='all':
        return True
    if st1==st2:
        return True
    else:
        return False

'''
type에 따른 특정 역의 승차, 하차 총 인원을 계산
'''
def countNumber(rows_get, type, station='all'):

    sum=0
    if type == 'r':
        str = '승차'
    elif type == 'd':
        str = '하차'

    row_len = len(rows_get)
    colunm_len = len(rows_get[0])

    # utf-8를 euc-kr로 변환
    euckr_str = unicode(str, 'utf-8').encode('euc-kr')

    for i in range(row_len):
        if (rows_get[i][2] == euckr_str) and (compareStr(rows_get[i][0], station)):
            #print unicode(rows_get[i][0], 'euc-kr').encode('utf-8') + '추가' ,
            for j in range(colunm_len-3):
                num = re.sub(",", "", rows_get[i][j+3])
                #print num ,
                sum += int(num)
            #print '\n'

    return  sum

'''
전체 역명을 리스트로 반환
'''
def listStation(rows_get, row_num):
    station_list=[]

    row_len = len(rows_get)
    for i in range(row_len-1):
        exist = False
        str = rows_get[i+1][row_num]
        #이미 존재하는지 검사
        for j in range(len(station_list)):
            exist = False
            if (str == station_list[j]):
                exist = True
        if (not exist):
                station_list.append(str)
                #print unicode(str, 'euc-kr').encode('utf-8'), '추가'

    print len(station_list)
    return station_list



def main() :

    rows=[]

    #csv 파일을 열고 열 획득
    f=open('riding_and_disembarking_passanger_201606.csv','r')
    csvReader=csv.reader(f)

    for row in csvReader:
        rows.append(row)

    f.close
    print "There are %d rows in list" %(len(rows))


    #승차 총 인원 출력
    riders = countNumber(rows, 'r')
    disembarker = countNumber(rows, 'd')

    print '승차 인원 : ', riders
    print '하차 인원 : ', disembarker

    stations = listStation(rows, 0)

    differ = {}

    for sta in range(len(stations)):
        numR = countNumber(rows, 'r', stations[sta])
        numD = countNumber(rows, 'd', stations[sta])
        print unicode(stations[sta], 'euc-kr').encode('utf-8'), ':', numR, '/', numD, '명 (', numD-numR, ')'
        if (numR-numD < 0):
            differ[stations[sta]] = numD-numR
        else:
            differ[stations[sta]] = numR-numD

    sorted_differ = sorted(differ.items(), key=operator.itemgetter(1))

    print numpy.array(sorted_differ)[:,0]
    print numpy.array(sorted_differ)[:, 1]


if __name__ == "__main__" :
    main()
