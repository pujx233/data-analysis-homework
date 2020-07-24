# coding=UTF-8
# @File:code_filter.py
# @Software: PyCharm
# @Description: 代码过滤,去掉cpp代码,面向用例代码和答案代码
import json


filter_code={}

def filter(path):
    fp=open(path,"r",encoding="utf8")
    data=json.load(fp)
    for key in data.keys():
        filter_code.setdefault(key,[])
        for item in data[key]["records"]:
            if(item["is_case-oriented"]==True) and (item["user_id"] not in filter_code[key]):
                filter_code[key].append(item["user_id"])
            if (item["is_cpp"]==True) and (item["user_id"] not in filter_code[key]):
                filter_code[key].append(item["user_id"])
            if "is_answer" in item.keys():
                if (item["is_answer"]==True) and (item["user_id"] not in filter_code[key]):
                    filter_code[key].append(item["user_id"])
    return filter_code









