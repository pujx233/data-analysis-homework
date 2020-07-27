"""
汇总了所有的统计前检测方法
包括检测是否抄袭答案，是否是非python代码，是否是面向用例

"""

import difflib
import os
import codeSimilarity.check_functions as cf


# 检测抄袭答案
def detect_is_answer(answerpath, codepath):
    similarity=cf.get_similarity(answerpath,codepath)
    if similarity >=90:
        return True
    else:
        return False

# 检测非python代码
def detect_no_py(filename):
    with open(filename, encoding="utf-8") as fp:
        content_list = fp.readlines()
        for content in content_list:
            content = content.strip()
            # 单独使用头文件判断 1429
            if content.startswith("#include"):

                return True
            # 1491
            if content.startswith("//") or content.startswith("/*") or content.startswith("<!--"):

                return True
            if content.startswith("private") or content.startswith("public") or content.startswith("protected"):

                return True
            # 1543
            if content.startswith("exec(bytes.from"):

                return True
            if content.startswith("if") and "//" in content and "(" in content and ":" not in content:

                return True

    return False


# 统计有效代码行数
def num_of_rows(fname):
    with open(fname, encoding='utf-8') as data:
        code_counts=0  #代码行数
        annotation_counts = 0  # 注释行数
        for file_line in data.readlines():
            # 统计注释行(一行中只有注释)
            if file_line.startswith('#'):
                annotation_counts += 1
            # 统计代码行
            elif file_line!=" ": #过滤空行
                code_counts += 1
    # 返回代码行数，注释行数
    return code_counts


# 检测面向用例
def detect_case_oriented(fname):
    with open(fname, encoding='utf-8') as data:
        code_counts=0  #有效代码行数
        nums=0 #以print开头的代码行数
        for file_line in data.readlines():
            if not file_line.startswith('#'): #过滤注释行
                if file_line!=" ": #过滤空行
                    code_counts += 1
                    if file_line.startswith('print'):
                        nums+=1
        if code_counts!=0 and nums/code_counts>0.3: #print语句占总语句的30%以上，判定为面向用例编程（系数待定）
            return True

    return False



