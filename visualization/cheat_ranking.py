# coding=UTF-8
# @File: cheat_ranking.py
# @Software: PyCharm
# @Description: 画抄袭人数最多的题目排名图和抄袭题目最多的学生排名图


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import matplotlib
import analysis.data_functions as df

#根目录
rPath=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))


matplotlib.rcParams['font.family']='STSong'
matplotlib.rcParams['font.size']=12
def plotCaseCheatRanking():
    data=df.case_cheat_ranking()
    X=data.keys()
    Y=data.values()
    plt.bar(X,Y,color='blue')
    plt.xlabel('题目ID')
    plt.ylabel('作弊人数')
    plt.title('抄袭人数最多的题目排名')

    for x, y in zip(X, Y):
        plt.text(x, y + 2.5, '%d' % y, ha='center', va='top')
    path = rPath + "/images/case_cheat_ranking.png"
    plt.savefig(path)
    plt.show()

def plotUserCheatRanking():
    data=df.user_cheat_ranking()
    X=data.keys()
    Y=data.values()
    plt.bar(X,Y,color='pink')
    plt.xlabel('学生ID')
    plt.ylabel('抄袭题目数量')
    plt.title('抄袭题目最多的学生排名')

    for x, y in zip(X, Y):
        plt.text(x, y + 3.5, '%d' % y, ha='center', va='top')

    path = rPath + "/images/user_cheat_ranking.png"
    plt.savefig(path)

    plt.show()





if __name__ == '__main__':
    plotUserCheatRanking()
    plotCaseCheatRanking()
