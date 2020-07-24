# coding=UTF-8
# @File: similarity.py
# @Software: PyCharm
# @Description: 画相似度数量分析的图
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import matplotlib
import analysis.data_functions as df

matplotlib.rcParams['font.family']='STSong'
matplotlib.rcParams['font.size']=14

filename="../data/code_similarity.xls"
data=pd.read_excel(filename)

print(data["相似度(87%以上)"].value_counts())
X=data["相似度(87%以上)"].value_counts().index
Y=data["相似度(87%以上)"].value_counts().values



# plt.bar(X,Y,color='blue')
# # plt.hist(data["相似度(87%以上)"],facecolor='blue',bins=13)
# plt.xlabel('代码相似度')
# plt.ylabel('数量')
# plt.title('相似度数量分析')
# plt.xticks(np.arange(86,103,1))
# plt.yticks(np.arange(0,2400,200))
# plt.xlim(86, 102)


fig, ax=plt.subplots()

rect1=ax.bar(X,Y)

ax.set_title(u'相似度数量分析')
ax.set_xlabel('代码相似度')
ax.set_ylabel('数量')
ax.set_xticks(np.arange(86,103,1))
ax.set_yticks(np.arange(0,2400,200))
for x, y in zip(X, Y):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x , y+100, '%d' % y, ha='center', va='top')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)

fig.tight_layout()
#根目录
rPath=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
path=rPath+"/images/similarity.png"
plt.savefig(path)
plt.show()



