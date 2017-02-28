# -*- coding: utf-8 -*-

'''
(1,1),(2,5),(3,6) 빨간 별모양 점찍기
scatter 함수 이용

ERROR
Traceback (most recent call last):
  File "scatter2.py", line 20, in <module>
    plt.scatter([(1,1)], 50, color ='red')
  File "/usr/lib/python2.7/site-packages/matplotlib/pyplot.py", line 3435, in scatter
    edgecolors=edgecolors, data=data, **kwargs)
  File "/usr/lib/python2.7/site-packages/matplotlib/__init__.py", line 1892, in inner
    return func(ax, *args, **kwargs)
  File "/usr/lib/python2.7/site-packages/matplotlib/axes/_axes.py", line 3958, in scatter
    raise ValueError("x and y must be the same size")
ValueError: x and y must be the same size

ERROR FIXED : chaged value of x, y in fuction scatter
              scatter([(1,1), (2,5), (3,6)], 50, color ='red')  ---> plt.scatter([1,2,3],[1,5,6], 100, color ='red')

'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.switch_backend('agg')

fig = plt.figure(figsize=(8,6), dpi=80)

# 정점 찍기
plt.scatter([1,2,3],[1,5,6], 100, color ='red',marker='*')

fig.savefig('scatter2.png')
