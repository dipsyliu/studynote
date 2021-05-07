#!/usr/bin/env python
# coding: utf-8

# In[147]:


import pandas as pd
import numpy as np
import random
import createdata_new
survey_num=createdata_new.survey_num #引入createdata_new.py文件中的survey_num变量，如果没有该文件可以直接赋值
#survey_num=100


# In[148]:


normal=pd.read_csv('normaldata.csv') #读取正态分布数据的文件
normal_arr=np.array(normal)

for k in range(1,survey_num+1):
    survey=pd.read_csv('survey '+str(k)+'.csv')
    survey_arr=np.array(survey)
    types=survey_arr[:,1]
    answer=survey_arr[:,2]
    blocks=survey_arr[:,3]
    
    n1=normal_arr[k-1,:]
    temp=[]
    index_4=[]
    index_23=[]
    count=0
    for i in range(len(types)):  #取出诈选题的分布位置
        if types[i]==4:
            index_4.append(i)

    for i in range(len(types)):
        if types[i]==2 or types[i]==3:
            index_23.append(i)
    
    temp=(n1.copy()).tolist()   #赋正态分布的值后再插入诈选题的值
    for j in index_4:
        temp.insert(j,random.randint(1,4))
        
    if len(index_23)==2:
        temp.insert(index_23[1],100*random.random())
    if len(index_23)==4:
        temp.insert(index_23[1],100*random.random())
        temp.insert(index_23[-1],100*random.random())
        
    dic1 = {'type_id': types, 'answer':temp, 'block_id': blocks }
    df = pd.DataFrame(dic1)
    filename='normal '+str(k)+'.csv'
    df.to_csv(filename,index=False)


# In[ ]:

