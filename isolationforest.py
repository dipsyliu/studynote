import re
import csv
import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest


def score(df, x):
    col = df[[str(x)]]
    col = col.drop(col[np.isnan(col[str(x)])].index)
    col = np.array(col)
    col.reshape(-1, 1)
    c = int(col.shape[0])
    # 如果整个属性无人评分
    if (c == 0):
        return (np.nan)
    model = IsolationForest(n_estimators=100,
                            max_samples='auto',
                            contamination=float(0.2),
                            max_features=1.0)
    model.fit(col)
    # depth：可信度（-不可信度），代表可信程度
    depth = -model.decision_function(col)

    # 归一化
    M = depth.max()
    m = depth.min()
    d_normal = np.zeros(depth.shape)
    for i in range(depth.shape[0]):
        d_normal[i] = (depth[i] - m) / (M - m)
    # 求得分
    i = 0
    j = 0
    h = 0
    while i < c:
        h = h + float(d_normal[i])
        j = j + float(col[i]) * float(d_normal[i])
        i = i + 1
    # df1=df[str(x)].describe()
    return (j / h)


x = 1
lista = []
df = pd.read_csv('./normaldata.csv')
while x <= 26:
    lista.append([])
    lista[x - 1].append('attribute%s' % str(x))
    lista[x - 1].append(score(df, x))
    out = open(r'./output.csv', 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    csv_write.writerow(lista[x - 1])
    x = x + 1
out.close()
print(lista)