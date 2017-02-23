# -*- coding: utf-8 -*-

'''
사인 코사인 그래프 그리기
그래프 속성 변경하기
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
plt.scatter([(1,1)], 50, color ='red')

fig.savefig('scatter2.png')