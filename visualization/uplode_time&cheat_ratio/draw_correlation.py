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


f = open('calendar_heat_map.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

ff = open('../../data/user_cheat_exercises.json', encoding='utf-8')
re = ff.read()
data_list = json.loads(re)

new_data = {}

for i in data:
    new_data[i] = {}
    new_data[i]["临时抱佛脚占比"] = data[i]["临时抱佛脚占比"]

for j in data_list:
    new_data[j]["抄袭占比"] = data_list[j]["total"]/200

save_as_file(new_data, 'correlation.json')
