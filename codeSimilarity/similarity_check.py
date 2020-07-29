
# coding=UTF-8
# @File: similarity_check.py
# @Software: PyCharm
# @Description: 代码查重


import os
import xlwt
import re
import multiprocessing
import json
import codeSimilarity.code_filter as cf
import codeSimilarity.check_functions as checks

#根目录
rPath=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

# 代码的父路径
mpath =rPath+"/LatestCodeDownload"

# 判决门限，指代码的相似度,找到相似度87%及以上的代码
gate = 87

#对代码行数超过10的文件进行查重
startLines=15


#每一份代码都有id,exerciseId,path
class StudentItem:
    def __init__(self):
        self.id = 0
        self.exerciseId=0
        self.lineNum=0
        self.path=""

#去除代码中的空行和注释
def filterFiles(cpath):
    acpath = mpath + "/" + cpath
    ccpaths = os.listdir(acpath)
    for ccpath in ccpaths:
        path = acpath + "/" + ccpath
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
                lines = fh.readlines()
        except IOError as ioerr:
            print('文件错误：' + str(ioerr))
            return None
        # 合并行
        source_code = ''
        for line in lines:
            new_line = re.sub(r'(\s|^)#.*', '', line)  # 去掉单行注释
            if re.search(r'(\w|\"|\')', new_line):  # 如果不是空白行
                source_code += new_line

        # 去掉 docstring
        source_code = re.sub(r'(\'{3}|\"{3}).*(\'{3}|\"{3})\s', '', source_code, flags=re.DOTALL)
        fh.close()
        try:
            with open(path, 'w', encoding='utf-8', errors='ignore') as file:
                file.write(source_code)
        except IOError as ioerr:
            print('文件错误：' + str(ioerr))
            return None
    print(cpath,"文件修改完成~")

def num_of_lines(path):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
            lines = fh.readlines()
    except IOError as ioerr:
        print('文件错误：' + str(ioerr))
        return None
    return len(lines)




def getCheatItems(cpath):

    acpath = mpath + "/" + cpath
    ccpaths=os.listdir(acpath)
    stu_items=[]
    for ccpath in ccpaths:
        path=acpath+"/"+ccpath
        # 为每一份代码设置一个Item并初始化
        stu_item = StudentItem()
        stu_item.id = ccpath.split('.')[0]
        stu_item.exerciseId = cpath
        stu_item.lineNum=num_of_lines(path)
        stu_item.path=path
        stu_items.append(stu_item)
    #找到不符合的代码
    dataPath = "../data/data_all.json"
    filter_code=cf.filter(dataPath)
    # 找到cheat_list
    cheat_list = []
    for stu_item1 in stu_items:
        for stu_item2 in stu_items:
            #去掉cpp,面向用例和答案代码
            if filter_code[stu_item1.exerciseId] and ((stu_item1.id in filter_code[stu_item1.exerciseId]) or (stu_item2.id in filter_code[stu_item1.exerciseId])):
                continue
            similarity = checks.get_similarity(stu_item1.path,stu_item2.path)
            if stu_item1.id != stu_item2.id and stu_item1.lineNum>startLines and stu_item2.lineNum>startLines and similarity > gate :
                if (stu_item1.exerciseId, stu_item2.id, stu_item1.id, similarity) not in cheat_list:
                    cheat_list.append((stu_item1.exerciseId, stu_item1.id, stu_item2.id, similarity))


    print(cpath, "完成~")
    return cheat_list

def main():
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # 创建一个workbook
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet',cell_overwrite_ok=True)
    #为worksheet设置行标题
    worksheet.write(0,0,label="题目ID")
    worksheet.write(0,1,label="用户1ID")
    worksheet.write(0, 2, label="用户2ID")
    worksheet.write(0, 3, label="相似度(87%以上)")
    count=0

    cpaths = os.listdir(mpath)
    # 对py文件进行预处理(去除空行和注释)(已进行预处理,故注释掉)
    # pool.map(filterFiles,cpaths)
    # print("文件修改完成")

    cheat_lists=pool.map(getCheatItems,cpaths)
    print(cheat_lists)
    #cheat: (题目ID,用户1,用户2,相似度)
    # 写入excel文件
    print("写入开始")
    for cheat_list in cheat_lists:
        for cheat in cheat_list:
            count=count+1
            worksheet.write(count, 0, cheat[0])
            worksheet.write(count, 1, cheat[1])
            worksheet.write(count, 2, cheat[2])
            worksheet.write(count, 3, cheat[3])
    print('完成写入')
    rPath=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    workbook.save(rPath+'/data/code_similarity.xls')

    #以题目id为索引写入抄袭用户
    exercise_cheat_users={}
    for cheat_list in cheat_lists:
        for cheat in cheat_list:
            exercise_cheat_users.setdefault(cheat[0],{})
            exercise_cheat_users[cheat[0]].setdefault("user_id",[])
            if cheat[1] not in exercise_cheat_users[cheat[0]]["user_id"]:
                exercise_cheat_users[cheat[0]]["user_id"].append(cheat[1])
            if cheat[2] not in exercise_cheat_users[cheat[0]]["user_id"]:
                exercise_cheat_users[cheat[0]]["user_id"].append(cheat[2])
    for key in exercise_cheat_users.keys():
        exercise_cheat_users[key]["total"]=len(exercise_cheat_users[key]["user_id"])

    exercise_cheat_users = dict(sorted(exercise_cheat_users.items(), key=lambda item: item[1]["total"], reverse=True))

    with open("../data/exercise_cheat_users.json","w", encoding="utf-8") as f:
        json.dump(exercise_cheat_users,f,indent=4)
        print("exercise_cheat_users 加载完成")

    #以用户id为索引写入用户抄袭的题目
    user_cheat_exercises={}
    for cheat_list in cheat_lists:
        for cheat in cheat_list:
            user_cheat_exercises.setdefault(cheat[1],{})
            user_cheat_exercises[cheat[1]].setdefault("case_id",[])
            if(cheat[0] not in user_cheat_exercises[cheat[1]]["case_id"]):
                user_cheat_exercises[cheat[1]]["case_id"].append(cheat[0])
            user_cheat_exercises.setdefault(cheat[2], {})
            user_cheat_exercises[cheat[2]].setdefault("case_id", [])
            if (cheat[0] not in user_cheat_exercises[cheat[2]]["case_id"]):
                user_cheat_exercises[cheat[2]]["case_id"].append(cheat[0])

    for key in user_cheat_exercises.keys():
        user_cheat_exercises[key]["total"]=len(user_cheat_exercises[key]["case_id"])

    user_cheat_exercises= dict(sorted(user_cheat_exercises.items(), key=lambda item: item[1]["total"], reverse=True))

    with open("../data/user_cheat_exercises.json","w",encoding="utf-8") as f:
        json.dump(user_cheat_exercises,f,indent=4)
        print("user_cheat_exercises 加载完成")


    #更新data_all.json

    fp=open("../data/data_all.json","r",encoding="utf-8")
    data=json.load(fp)
    fp.close()
    fp_2=open("../data/exercise_cheat_users.json","r",encoding="utf-8")
    data_users=json.load(fp_2)
    fp_2.close()
    for key in data.keys():
        num_of_iscopy=0
        for index,item in enumerate(data[key]["records"]):
            if (key in data_users.keys()):
                if(item["user_id"] in data_users[key]["user_id"]):
                    data[key]["records"][index]["is_copy"]=True
                    num_of_iscopy+=1
                else:
                    data[key]["records"][index]["is_copy"] = False
            else:
                data[key]["records"][index]["is_copy"] = False
        data[key]["num_of_iscopy"]=num_of_iscopy

    with open("../data/data_all.json","w",encoding="utf-8") as fp_3:
        json.dump(data,fp_3,ensure_ascii=False,indent=4)

if __name__ == '__main__':
    main()















