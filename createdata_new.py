#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
import pandas as pd
import random


# In[31]:


def generate_surnum():
    global survey_num
    survey_num=100
    return survey_num


# In[32]:


def type1(types):
    ques=[]
    cheat=[]
    for i in range(2):
        rele=[]
        m=1+i*13
        n=13+i*13
        seg=list(range(m,n))
        cheat.append(random.randint(2,4))
        if cheat[i]!=4:
            random.shuffle(seg)
            for j in range(2):
                rele.append(seg[j])
            ques.append(rele)
            types.insert(rele[1],cheat[i])
            types[rele[0]]=cheat[i]
        else:
            a=random.choice(range(m,n))
            ques.append(a)
            types.insert(a,cheat[i])
    return(types)


# In[38]:


def answer1():
    answer=[]
    for i in range(len(types)):
        answer.append(0)
    return(answer)


# In[17]:


def block1():
    block=[]
    for i in range(2):
        m=1+i*14
        n=15+i*14    
        for j in range(m,n):
            block.append(i)
    return(block)


# In[39]:


generate_surnum()
for k in range(1,survey_num+1):
    index=list(range(1,29))
    types_array=np.ones(26,int)
    types=types_array.tolist()
    blocks=block1()
    types=type1(types)
    answers=answer1()
    dic1 = { 'question_id': index, 'type_id': types, 'answer':answers, 'block_id': blocks }
    df = pd.DataFrame(dic1)
    filename='survey '+str(k)+'.csv'
    df.to_csv(filename,index=False)


# In[ ]:



