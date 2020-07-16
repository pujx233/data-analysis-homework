
# coding=UTF-8
# @File: similarity_check.py
# @Software: PyCharm
# @Description: 代码查重
# @dataSource:使用CodeDownload.py按照目录下载用户最后一次提交代码


import os
import ssdeep
import xlwt
import re
import multiprocessing


# 代码的父路径
mpath = "D:/Custom_Files/大二下\新建文件夹/data-analysis-homework/LatestCodeDownload"

# 判决门限，指代码的相似度,找到相似度70%及以上的代码
gate = 70

#对代码行数超过10的文件进行查重
startLines=10

#每一份代码都有id,exerciseId,hash
class StudentItem:
    def __init__(self):
        self.id = 0
        self.exerciseId=0
        self.lineNum=0
        self.hash = ""

#去除代码中的空行和注释并返回代码函数
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


#获得py文件的哈希值
def get_hash(path):
    f = open(path, 'r',encoding='UTF-8')
    lines = [l.strip() for l in f.readlines()]
    codes = ""
    for line in lines:
        codes += line
    return ssdeep.hash(codes)

#根据文件路径比较两个文件的哈希值
def compare(path1, path2):
    hash1 = get_hash(path1)
    hash2 = get_hash(path2)
    return ssdeep.compare(hash1, hash2)

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
        stu_item.hash = get_hash(path)
        stu_items.append(stu_item)
    # 找到cheat_list
    cheat_list = []
    for stu_item1 in stu_items:
        for stu_item2 in stu_items:
            similarity = ssdeep.compare(stu_item1.hash, stu_item2.hash)
            if stu_item1.id != stu_item2.id and stu_item1.lineNum>startLines and stu_item2.lineNum>startLines and similarity > gate :
                if (stu_item1.exerciseId, stu_item2.id, stu_item1.id, similarity) not in cheat_list:
                    cheat_list.append((stu_item1.exerciseId, stu_item1.id, stu_item2.id, similarity))
    # cheat_lists.extend(cheat_list)

    print(cpath, "完成~")
    return cheat_list

if __name__ == '__main__':
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # 创建一个workbook
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet',cell_overwrite_ok=True)
    #为worksheet设置行标题
    worksheet.write(0,0,label="题目ID")
    worksheet.write(0,1,label="用户1ID")
    worksheet.write(0, 2, label="用户2ID")
    worksheet.write(0, 3, label="相似度(70%以上)")
    count=0

    cpaths = os.listdir(mpath)
    # 对py文件进行预处理(去除空行和注释)(已进行预处理,故注释掉)
    pool.map(filterFiles,cpaths)
    print("文件修改完成")
    cheat_lists=pool.map(getCheatItems,cpaths)
    print(cheat_lists)
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
    workbook.save('data.xls')

