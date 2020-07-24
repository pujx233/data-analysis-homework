import json
import os


#根目录
rPath=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

# 代码的父路径
mpath =rPath+"/LatestCodeDownload"


#获得作弊代码总数量
def getCheatCodeNums():
    codeNums=0
    with open("../data/exercise_cheat_users.json") as fp:
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
    with open("../data/user_cheat_exercises.json") as fp:
        data=json.load(fp)
    return len(data.keys())

#获得抄袭人数最多的题目排名
def case_cheat_ranking():
    ranks={}
    with open("../data/exercise_cheat_users.json") as fp:
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
    with open("../data/user_cheat_exercises.json") as fp:
        data = json.load(fp)
        count = 0
        for key in data.keys():
            ranks[key] = data[key]["total"]
            count = count + 1
            if (count >= 10):
                break
    return ranks

