'''
y = 0 + 1 + 2 + 3 + ...n 's  graph

'''

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.switch_backend('agg')

max=50
x = np.arange(max)
y = []

y.append(0)


for i in range(1, len(x)):
    y.append(y[i-1]+i)

print 'Y = ', y
fig = plt.figure()

plt.plot(x, y, label='SUMMATION')
plt.scatter(x, y, 10, color='red')

for i in range(len(x)/5):
    j=i*5
    plt.plot([0, j],[y[j], y[j]], color ='gray', linewidth=1.0, linestyle="--")
    plt.plot([x[j], x[j]], [0, y[j]], color='gray', linewidth=1.0, linestyle="--")


plt.xlim(0, len(x))
plt.ylim(0, y[max-1])

plt.title('SUMMATION')


fig.savefig('summation.png')