'''
summation program

print 1+2+3+...+n
'''

s = input('Enter number : ')

sum = 0
for i in range (1, s+1):
	sum += i	

print 'summation is ', sum 
