# coding=UTF-8
# @File: cheat_ratio.py
# @Software: PyCharm
# @Description: 画作弊人数占比和作弊题目占比的图

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import matplotlib
import analysis.data_functions as df

matplotlib.rcParams['font.family']='STSong'
matplotlib.rcParams['font.size']=14

#根目录
rPath=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

# 代码的父路径
mpath =rPath+"/LatestCodeDownload"

def code_cheat_ratio():
    codeTotal=df.getCodeTotal()
    cheatNums=df.getCheatCodeNums()

    print(cheatNums)
    print(codeTotal)

    ratio=round(cheatNums/codeTotal*100*10)/10

    remain=100-ratio

    print(ratio)
    print(remain)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = '作弊代码', '未作弊代码'
    sizes = [ratio,remain]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
             startangle=180,colors=['red','blue'])
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


    path=rPath+"/images/code_cheat_ratio.png"
    plt.savefig(path)
    plt.show()


def user_cheat_ratio():
    userTotal = df.getUserTotal()
    userNums = df.getCheatUserNums()

    print(userNums)
    print(userTotal)

    ratio = round(userNums / userTotal * 100 * 10) / 10

    remain = 100 - ratio

    print(ratio)
    print(remain)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = '作弊人数', '未作弊人数'
    sizes = [ratio, remain]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            startangle=180, colors=['red', 'cyan'])
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    path = rPath + "/images/user_cheat_ratio.png"
    plt.savefig(path)
    plt.show()


if __name__ == '__main__':
    user_cheat_ratio()
    # code_cheat_ratio()






