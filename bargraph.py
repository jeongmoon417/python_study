# -*- coding: utf-8 -*-

'''
막대 그래프 예제
랜덤 수 n개를 막대 그래프로 표현
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
import matplotlib.pyplot as plt


plt.switch_backend('agg')

fig = plt.figure()

n = 12
X = np.arange(n)    #[0,1,2,3,...,10,11]
Y1 = (1-X/float(n)) * np.random.uniform(0.5, 1.0, n)
#Y1 = (1-X/float(n))

print Y1

plt.axes([0.1, 0.1, 0.9, 0.9])
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')

for x,y in zip(X, Y1):
    plt.text(x, y+0.05, '%.2f' %y, ha='center', va='bottom')

plt.xlim(-.5,n)
plt.xticks(range(0, n))
plt.ylim(0, +1.25)
plt.yticks(np.arange(0, 1.3, 0.1))

fig.savefig('bargraph.png')