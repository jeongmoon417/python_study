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

# 8X6포인트, 100 dots/inch 의 새로운 피규어(figure) 생성
fig = plt.figure(figsize=(8,6), dpi=80)

# 1X1 그리드의 새로운 서브플롯(subplot) 생성????
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

# 사인 그래프 : 빨간색, 두깨 1픽셀, 끊김이 없는 라인
plt.plot(X, S, color="red", linewidth=1.5, linestyle="-", label="sine")
# 코사인 그래프 : 파란색, 두깨 1픽셀, 끊김이 없는 라인
plt.plot(X, C, color="blue", linewidth=1.5, linestyle="-", label='cosine')

# X의 끝점(limit) 설정
plt.xlim(-4.0, 4.0)

# x ticks을 설정 -> 숫자들
#plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# Y의 끝점 설정
plt.ylim(-1.0, 1.0)

# y ticks을 설정
#plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

#x축과 y축을 설정
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))


t=2*np.pi/3
# 정점 찍기
plt.scatter([t,],[np.sin(t),], 50, color ='red')
# 점선 그리기
plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.0, linestyle="--")
#화살표와 글 쓰기
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


plt.legend(loc = 'upper left', frameon=False)

fig.savefig('sincos_setting.png')
