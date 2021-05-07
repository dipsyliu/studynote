#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
forest=pd.read_csv('forest .csv')
forest_arr=np.array(forest)
score=forest_arr[:,1].tolist()
ques_id=[8,10,11,12,13,14,15,16,19,20,21,22,23,24,26,27,28,30,31,32,33,34,36,37,38,39]
leaf_weight=[15,30,45,45,45,60,60,15,30,30,45,45,45,15,15,30,30,15,15,45,45,45,10,30,30,30]
leaf_score=[score[i]*leaf_weight[i] for i in range(len(score))]
leaves_id = [str(x) for x in ques_id]

plt.figure(figsize=(20,10))
plt.xlabel('leaves_id',fontsize=17)
plt.ylabel('score',fontsize=17)
plt.title('forest',fontsize=20)                                                                 #根据不同的五大类题型给相应的子题目标上不同的颜色
plt.bar(leaves_id,leaf_score,color=['c','c','c','c','c','c','c','g','g','g','g','g','g','b','b','b','b','pink','pink','pink','pink','pink','orange','orange','orange','orange'],alpha=0.6)
plt.tick_params(labelsize=15)

for a,b in zip(leaves_id,leaf_score):   #显示柱状图上的数字
    plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=14);
    
plt.show()

plt.savefig('forest_score.png')

dic = {'question':range(1,len(ques_id)+1),'leaves_id':ques_id,'score': leaf_score }
df = pd.DataFrame(dic)
df.to_csv('final_score.csv',index=False)


# In[ ]:




