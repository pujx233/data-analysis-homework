import json
import os
import numpy as np


#根目录
rPath=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

# 代码的父路径
mpath =rPath+"/LatestCodeDownload"


#获得作弊代码总数量
def getCheatCodeNums():
    codeNums=0
    with open("../data/exercise_cheat_users.json","r",encoding="utf-8") as fp:
        data=json.load(fp)
        for key in data.keys():
            codeNums=codeNums+data[key]["total"]
    return codeNums


#获得代码总数量
def getCodeTotal():
    codeTotal=0
    for cpath in os.listdir(mpath):
        acpath =mpath  + "/" + cpath
        codeTotal=codeTotal+len(os.listdir(acpath))
    return codeTotal

#获得用户总数量
def getUserTotal():
    users=[]
    for cpath in os.listdir(mpath):
        acpath = mpath + "/" + cpath
        for ccpath in os.listdir(acpath):
            user=ccpath.split('.')[0]
            if(user not in users):
                users.append(user)
    return len(users)

#获得作弊用户数量
def getCheatUserNums():
    with open("../data/user_cheat_exercises.json","r",encoding="utf-8") as fp:
        data=json.load(fp)
    return len(data.keys())

#获得抄袭人数最多的题目排名
def case_cheat_ranking():
    ranks={}
    with open("../data/exercise_cheat_users.json","r",encoding="utf-8") as fp:
        data = json.load(fp)
        count=0
        for key in data.keys():
            ranks[key]=data[key]["total"]
            count=count+1
            if(count>=10):
                break
    return ranks


#获得抄袭题目最多的学生排名
def user_cheat_ranking():
    ranks = {}
    with open("../data/user_cheat_exercises.json","r",encoding="utf-8") as fp:
        data = json.load(fp)
        count = 0
        for key in data.keys():
            ranks[key] = data[key]["total"]
            count = count + 1
            if (count >= 10):
                break
    return ranks

def get_cheat_ratio_difficulty():
    temp={}
    fp=open("../data/simplified_data.json","r",encoding="utf-8")
    data=json.load(fp)
    for case_id, details in data.items():
        cheat_ratio=round(details["num_of_isco"]/details["user_count"]*100)
        temp.setdefault(details["difficulty"],[])
        temp[details["difficulty"]].append(cheat_ratio)

    difficultys=[]
    cheat_ratios=[]
    temp=dict(sorted(temp.items(),key=lambda item:item[0]))
    for difficulty,arrays in temp.items():
        avg=round(np.mean(arrays))
        difficultys.append(difficulty)
        cheat_ratios.append(avg)
    return difficultys,cheat_ratios










