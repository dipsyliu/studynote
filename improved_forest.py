#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import random
import math
import collections
import createdata_new
survey_num=createdata_new.survey_num #引入createdata_new.py文件中的survey_num变量，如果没有该文件可以直接赋值
treshold=5 #若数据量小于该阈值，则考虑所有数据都作为根节点的情况
root_rate=0.6 #数据量大于阈值时作为根节点的数据所占的比例
ques_num = 26 #问卷题数


# In[2]:

def findSmallest(arr):
    smallest = arr[0]      #存储最小的值
    smallest_index = 0     #存储最小元素的索引
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
#选择排序
def selectionSort(arr):   #对数组进行排序
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))   #找出数组中最小的元素，并将其加入到新数组中
    return newArr


# In[9]:


def sort(arr,level): #将每一层的节点依次分为左右两组
    while len(arr)>1:
        arr1=[]
        arr2=[]
        for k in range(math.ceil(len(arr)/2)):
            arr1.append(arr[k])
        arr2=list(set(arr1) ^ set(arr))
        level+=1
        
        if len(arr2)==1:
            dict1[arr2[0]]=level
        else:
            sort(arr2,level)
            
        if len(arr1)==1:
            dict1[arr1[0]]=level
        else:
            sort(arr1,level)
            
        arr=min(arr1,arr2)



# In[4]:


def duplicate(arr):   #找出重复的数据
    import collections
    duplication=[item for item, count in collections.Counter(arr).items() if count> 1]
    return duplication


# In[5]:


def dup_index(duplic,data_0): #找出重复的数据对应的数组下标
    index=[]
    for i in range(len(data_0)):
        for j in range(len(duplic)):
            if data_0[i]==duplic[j]:
                index.append(i)
    return index


# In[6]:


def add_noise(duplic,data0):    #给重复的数据加一个小的random扰动
    data1=data0.copy()
    error=0.1        
    for x in range(len(data1)):
        for y in range(len(duplication)):           
            if data1[x]==duplication[y]: 
                data1[x]+=error*random.random()
    return data1


# In[7]:


def scoring(scores,indexes): #最后的权重同一个重复点的第二阶段要加权平均

    if len(indexes)!=0:  
        sum=0
        average=0
        for x in indexes:
            sum+=scores[x]
        average=sum/len(indexes)
        for x in indexes:
            scores[x]=average
    return scores         


# In[24]:

score = []

for item in range(ques_num):  # 循环问卷中的26道题
    data = []
    data0 = []
    data1 = []
    weight = []
    weight0 = []
    level = 1
    dict = {}
    dict1 = {}
    for k in range(1, survey_num + 1):
        IWA = pd.read_csv('IWA ' + str(k) + '.csv')
        IWA_arr = np.array(IWA).tolist()
        data.append(IWA_arr[item][2])  # 第k份问卷的第item道题的答案
        weight.append(IWA_arr[item][1])  # 第k份问卷的第item道题的权重

    data = selectionSort(data)  # 将data进行从小到大的重排序
    if len(data) > treshold:  # 当数据大于一定阈值的时候随机选取一部分数据小标作为根节点下标
        index_1 = random.sample(list(range(len(data))), int(len(data) * root_rate))
        index_1 = selectionSort(index_1)  # 随机选取根节点下标，并进行从小到大的排序
        for x in index_1:
            data0.append(data[x])  # 将随机选取的根节点小标对应的答案和权重分别存入data0和weight0
            weight0.append(weight[x])
    else:
        data0 = data

    duplication = duplicate(data0)  # 找出根节点中重复的值
    index = dup_index(duplication, data0)  # 找出重复的根节点所对应的数组下标
    data1 = add_noise(duplication, data0)  # 给重复的数据加一个小的random扰动，data1为加了扰动后的没有重复值的根节点
    node_num = len(data1)
    for i in range(len(data1)):
        left = []
        right = []
        dict1 = {}
        for j in range(len(data1)):

            if data1[j] <= data1[i]:
                left.append(data1[j])  # 小于等于根节点的值归于left，大于根节点的值归于right
            else:
                right.append(data1[j])

        if len(left) == 1:
            dict1[left[0]] = level + 1
        if len(right) == 1:
            dict1[right[0]] = level + 1
        sort(left, level + 1)
        sort(right, level + 1)
        dict[data1[i]] = dict1

    sub_dict = []
    for key, values in dict.items():
        sub_dict.append(values)

    order_sub = []  # 重新排列sub_dict
    for i in range(len(sub_dict)):
        a = {k: v for k, v in sorted(sub_dict[i].items(), key=lambda item: item[0])}
        order_sub.append(a)

    a_value = []
    value = []  # 提取相对应的深度
    for i in range(len(order_sub)):
        for key, values in order_sub[i].items():
            a_value.append(values)
        value.append(a_value)
        a_value = []

    s1 = 0
    s2 = 0
    score1 = []
    score2 = []  # 两种方法计算出score
    for i in range(len(value[0])):
        for j in range(len(value)):
            s1 += value[j][i]
            if value[j][i] == 2:
                s = 1
            else:
                s = 2 / (value[j].count(value[j][i]) * node_num)
            s2 += s
        score1.append(s1 / node_num)
        score2.append(s2 / node_num)
        s1 = 0
        s2 = 0

    score1 = scoring(score1, index)
    score2 = scoring(score2, index)

    s1_x = 0
    s2_x = 0
    sum1 = 0
    sum2 = 0
    for j in range(len(score1)):  # 每个根节点与其对应的s1乘积之和除以所有s1和，
        # 再加上每个根节点与其对应的s2乘积之和除以所有s2和的商指和的1/2，为最终score
        s1_x += score1[j] * data0[j] * weight0[j]
        sum1 += score1[j] * weight0[j]  # score1[j]乘上对应的权重weight0[j]
        s2_x += score2[j] * data0[j]
        sum2 += score2[j]

    score.append((s1_x / sum1 + s2_x / sum2) / 2)

dic2 = {'question': range(1, ques_num + 1), 'score': score}
df1 = pd.DataFrame(dic2)
filename = 'forest ' + '.csv'
df1.to_csv(filename, index=False)

# In[82]:


