# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
# matplotlib画图中中文显示会有问题，需要这两行设置默认字体

plt.xlabel('X')
plt.ylabel('Y')
#plt.xlim(xmax=9, xmin=0)
#plt.ylim(ymax=9, ymin=0)
# 画两条（0-9）的坐标轴并设置轴标签x，y

x1 = np.random.normal(2, 0.5, 500)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的x轴坐标
y1 = np.random.normal(2, 0.5, 500)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的y轴坐标
x2 = np.random.normal(6, 0.8, 300)
y2 = np.random.normal(6, 0.8, 300)
x3 = np.random.normal(4 ,0.1 ,10)
y3 = np.random.normal(4 ,0.1 ,10)
x4 = np.random.normal(9 ,0.1 ,10)
y4 = np.random.normal(2 ,0.1 ,10)
x5 = np.random.normal(2 ,0.1 ,1)
y5 = np.random.normal(9 ,0.1 ,1)
x6 = np.random.normal(5 ,0.1 ,1)
y6 = np.random.normal(1 ,0.1 ,1)

colors1 = '#00CED1'  # 点的颜色
colors2 = '#DC143C'
colors3 ='#8A2BE2'
area = np.pi * 4 ** 2  # 点面积
# 画散点图
plt.scatter(x1, y1, s=area, c=colors1, alpha=0.4, label='normal points')
plt.scatter(x2, y2, s=area, c=colors1, alpha=0.4)
plt.scatter(x3, y3, s=area, c=colors2, alpha=0.4, label='clustered anomalies')
plt.scatter(x4, y4, s=area, c=colors2, alpha=0.4)
plt.scatter(x5, y5, s=area, c=colors3, alpha=0.4, label='scattered anomalies')
plt.scatter(x6, y6, s=area, c=colors3, alpha=0.4)
#plt.plot([0, 9.5], [9.5, 0], linewidth='0.5', color='#000000')
plt.legend()
plt.savefig(r'D:\dipsy liu\Zyouke\12345svm.png', dpi=300)
plt.show()