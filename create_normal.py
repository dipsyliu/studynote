#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import createdata_new
survey_num=createdata_new.survey_num #引入createdata_new.py文件中的survey_num变量，如果没有该文件可以直接赋值
#survey_num = 100  # 问卷数
# random_rate=0.25     #25%的乱填率
averages = pd.read_csv('averages.csv')
averages_np = np.array(averages)
(l, c) = np.shape(averages_np)
for i in range(l):
    # 以规定的均值为中心，生成正态分布数据
    average = averages_np[i, :]
    M = np.random.normal(-10, 5, [survey_num, c])
    N = np.random.normal(10, 5, [survey_num, c])
    for j in range(c):
        M[:, j] = M[:, j] + average[j] +N[:,j]
    low0 = np.where(M < 0)
  #  M[low0[0], low0[1]] = np.NAN
    M[low0[0], low0[1]] = 0
    # 比0低和比1高的数据改为空值
    high1 = np.where(M > 100)
    M[high1[0], high1[1]] = 100
    lens=len(average)
    
    # 有0.1概率某属性无人填写
    # for k in range(10):
    #     randNum = np.random.rand()
    #     if randNum < 0.1:
    #         M[:, k] = np.NAN
    outpath = './normaldata' + '.csv'
    M_out = pd.DataFrame(M, columns=range(1, 27))
    M_out.to_csv(outpath, index=False)

