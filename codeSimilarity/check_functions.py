# coding=UTF-8
# @File: check_function.py
# @Software: PyCharm
# @Description: 代码查重的具体函数



import difflib
import ssdeep

#第一种方法
# 检测抄袭答案
def detect_is_answer(path1, path2):
    def get_similarity_ratio(s, t):
        return difflib.SequenceMatcher(None, s, t).quick_ratio()

    similarity_ratio = get_similarity_ratio(path1, path2)
    return round(similarity_ratio*100)


#第二种方法:ssdeep
#获得py文件的哈希值
def get_hash(path):
    f = open(path, 'r',encoding='utf-8')
    lines = [l.strip() for l in f.readlines()]
    codes = ""
    for line in lines:
        codes += line
    return ssdeep.hash(codes)

#根据文件路径比较两个文件的哈希值
def ssdeep_compare(path1, path2):
    hash1 = get_hash(path1)
    hash2 = get_hash(path2)
    return ssdeep.compare(hash1, hash2)



#为两种方法赋予不同权重
def get_similarity(path1,path2):
    ssdeep_score=ssdeep_compare(path1,path2)
    difflib_score=detect_is_answer(path1,path2)
    if(ssdeep_score==100):
        return round(ssdeep_score)
    else:
        score=ssdeep_score*0.2+difflib_score*0.8
        return round(score)



def get_cheat_html(path1,path2):
    diff = difflib.HtmlDiff()
    fp = open(path1, "r", encoding="utf-8")
    data_1 = fp.readlines()
    fp.close()

    fp_2 = open(path2, "r", encoding="utf-8")
    data_2 = fp_2.readlines()
    fp_2.close()

    content = diff.make_file(data_1, data_2)

    with open("../data/test.html", 'w', encoding="utf-8") as f:
        f.write(content)


path1="../LatestCodeDownload/2061/60635.py"
path2="../LatestCodeDownload/2061/49405.py"

detect_is_answer(path1,path2)
# print(ssdeep_compare(path1,path2))