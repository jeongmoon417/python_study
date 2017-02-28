import sys
reload(sys)
sys.setdefaultencoding('utf8')

'''
pie graph exercise
'''

import matplotlib.pyplot as plt

plt.switch_backend('agg')
fig = plt.figure()

labels = 'Mango', 'Strawberry', 'Graph', 'Banana', 'Tomato'
sizes = [12, 37, 29, 13, 5]
colors = ['#ff9e9b', '#ffa8a5',  '#ffb2af',  '#ffbcb9',  '#ffc6c3']
explode = (0, 0.1, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')

fig.savefig('piechart.png')
