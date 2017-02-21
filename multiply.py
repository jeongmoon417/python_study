'''
multiply program

print 1*n, 2*n, 3*n, ..., n*n
'''

s = input('Enter some number : ')
if (s>0 or s<10) :
        for i in range(1,10):
                print '%d*%d=%d' %(s, i, i*s)
