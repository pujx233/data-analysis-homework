import urllib.request, urllib.parse
import os
import json


def save_as_file(data: dict, filename):
    """
    存档
    :param data: 需要保存的数据（字典格式）
    :param filename: 应保存的文件名
    :return:
    """
    with open(filename, 'w', encoding='utf-8')as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


f = open('../data/data_all.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
data = list(dict.values(data))

user_data = {}

for da in data:
    records = da["records"]
    case_id = da["case_id"]
    for record in records:
        user_id = record["user_id"]
        if user_id not in user_data.keys():
            user_data[user_id] = {}
        user_data[user_id][case_id] = {}
        user_data[user_id][case_id]["final_score"] = record["final_score"]
        user_data[user_id][case_id]["case_type"] = da["case_type"]
        user_data[user_id][case_id]["upload_times"] = record["upload_times"]
        user_data[user_id][case_id]["final_upload_id"] = record["final_upload_id"]
        user_data[user_id][case_id]["num_of_line"] = record["num_of_line"]
        user_data[user_id][case_id]["is_cpp"] = record["is_cpp"]
        user_data[user_id][case_id]["is_case-oriented"] = record["is_case-oriented"]
        user_data[user_id][case_id]["is_answer"] = record["is_answer"]
        user_data[user_id][case_id]["is_copy"] = record["is_copy"]
        user_data[user_id][case_id]["is_valid"] = record["is_valid"]
        user_data[user_id][case_id]["revised score"] = record["final_score"]
        if user_data[user_id][case_id]["is_answer"] or user_data[user_id][case_id]["is_copy"] or \
                user_data[user_id][case_id]["is_case-oriented"] or user_data[user_id][case_id]["is_cpp"]:
            user_data[user_id][case_id]["revised score"] = 0
        if user_data[user_id][case_id]["is_valid"] == False:
            user_data[user_id][case_id]["revised score"] = 0

save_as_file(user_data, '../data/user_data.json')
