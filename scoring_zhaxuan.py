#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import random
import createdata_new
constant_nw=1 #错题阈值 
CONSTANT_W=0.5 #降低权重
constant1=0.8 #相似度
survey_num=createdata_new.survey_num #引入createdata_new.py文件中的survey_num变量，如果没有该文件可以直接赋值
ques_id=[8,10,11,12,13,14,15,16,19,20,21,22,23,24,26,27,28,30,31,32,33,34,36,37,38,39]#根据叶子节点的标识数作为题号


# In[2]:


def leaf_weight(answer0):
    for y in range(len(q_id)):
        if q_id[y]==8 or q_id[y]==16 or q_id[y]==24 or q_id[y]==26 or q_id[y]==30 or q_id[y]==31:
            result.append(answer[y]*(1/15))
        elif q_id[y]==10 or q_id[y]==19 or q_id[y]==20 or q_id[y]==27 or q_id[y]==28 or q_id[y]==37 or q_id[y]==38 or q_id[y]==39:
            result.append(answer[y]*(1/30))
        elif q_id[y]==11 or q_id[y]==12 or q_id[y]==13 or q_id[y]==21 or q_id[y]==22 or q_id[y]==23 or q_id[y]==32 or q_id[y]==33 or q_id[y]==34:
            result.append(answer[y]*(1/45))
        elif q_id[y]==14 or q_id[y]==15:
            result.append(answer[y]*(1/60))
        elif q_id[y]==36:
            result.append(answer[y]*0.1)
    return(result)


# In[3]:


def add(x):
    IWA.append(1)
    b_id.append(int(block[x]))


# In[4]:


def question_id(zhaxuan):#给诈选题的问题编号标记为0，和普通题区分开
    q_id=ques_id.copy()
    for z in range(len(zhaxuan)):
        q_id.insert(zhaxuan[z],0)
    return q_id

# In[5]:


def type3(fir3): #逆向关联题评分
    global num_w
    sim3_1=answer[fir3]+answer[i]
    sim3_2=200-(answer[fir3]+answer[i])
    sim3=min(sim3_1,sim3_2)
    if sim3<constant1:
        num_w+=1 
        block_w.append(block[i])


# In[6]:


def type2(fir2): #正向关联题评分
    global num_w
    sim2=(100-abs(answer[fir2]-answer[i]))/100
    if sim2<constant1:                      
        num_w+=1 
        block_w.append(block[i])


# In[7]:
count4=0
count23=0

for k in range(1, survey_num + 1):
    survey = pd.read_csv('normal ' + str(k) + '.csv')
    survey_arr = np.array(survey)
    types = survey_arr[:, 0]
    answer = survey_arr[:, 1]
    block = survey_arr[:, 2]
    num_w = 0
    num_rele = 0
    IWA = []
    b_id = []
    result = []
    block_rele = []
    block_w = []
    zhaxuan = []
    right_an = random.randint(1, 4)  # 用随机生成的整数暂代常识题的答案，如果之后有常识题答案的数据可以导入替换该处
    for i in range(len(types)):
        if types[i] != 1:
            if types[i] == 4:  # 常识题判断
                count4 += 1
                zhaxuan.append(i)
                if answer[i] != right_an:
                    num_w += 1
                    block_w.append(block[i])
                    continue
            else:
                count23 += 1
                block_rele.append(block[i])
                if block_rele[-1] != block_rele[len(block_rele) - 2]:
                    num_rele = 0

                if num_rele < 1:  # 寻找相对应的关联题的两个题号
                    add(i)
                    fir_rele = i
                    num_rele += 1
                else:
                    zhaxuan.append(i)
                    if types[i] == 2:
                        type2(fir_rele)
                    else:
                        type3(fir_rele)
                    continue

        else:
            add(i)

    q_id = question_id(zhaxuan)
    result = leaf_weight(answer)
    if num_w <= constant_nw and num_w != 0:
        for i in range(len(IWA)):
            if b_id[i] == block_w[0] or b_id[i] == block_w[-1]:
                IWA[i] = IWA[i] * CONSTANT_W  # 给没有超过错题阈值的有诈选题错误的部分降低权重
    elif num_w > constant_nw:
        IWA = [0 for j in range(len(IWA))]

    dic2 = {'question_id': ques_id, 'weight': IWA, 'answer': result, 'block_id': b_id}
    df2 = pd.DataFrame(dic2)
    df2.index = range(1, len(df2) + 1)
    filename = 'IWA ' + str(k) + '.csv'
    df2.to_csv(filename, index=False)




