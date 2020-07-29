#此为生成实际过滤后的最终得分

import urllib.request, urllib.parse
import os
import json


class AutoVivification(dict):
    """生成嵌套字典"""

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


dir = AutoVivification()
case_id_list = []
with open("../data/user_data.json", 'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
for i in load_dict:  # i为学生id j为case_id
    # dir[i]['用户编号'] = i['user_id']
    dir[i]['字符串平均得分'] = 0
    dir[i]['字符串提交次数'] = 0
    dir[i]['图结构平均得分'] = 0
    dir[i]['图结构提交次数'] = 0
    dir[i]['树结构平均得分'] = 0
    dir[i]['树结构提交次数'] = 0
    dir[i]['数字操作平均得分'] = 0
    dir[i]['数字操作提交次数'] = 0
    dir[i]['排序算法平均得分'] = 0
    dir[i]['排序算法提交次数'] = 0
    dir[i]['查找算法平均得分'] = 0
    dir[i]['查找算法提交次数'] = 0
    dir[i]['数组平均得分'] = 0
    dir[i]['数组提交次数'] = 0
    dir[i]['线性表平均得分'] = 0
    dir[i]['线性表提交次数'] = 0
    dir[i]['score'] = [dir[i]['字符串平均得分'], dir[i]['图结构平均得分'], dir[i]['树结构平均得分'], dir[i]['数字操作平均得分'], dir[i]['排序算法平均得分'],
                       dir[i]['查找算法平均得分'], dir[i]['数组平均得分'], dir[i]['线性表平均得分']]

for i in load_dict:  # i为学生id j为case_id
    num = len(load_dict[i])
    dir[i]['提交习题'] = num
    dir[i]['提交占比'] = num/200
    num = 0
    for j in load_dict[i]:
        if  load_dict[i][j]["case_type"] == '字符串':
            dir[i]['字符串提交次数'] += 1
            dir[i]['字符串平均得分'] += load_dict[i][j]['revised score']
        if load_dict[i][j]["case_type"] == '图结构':
            dir[i]['图结构提交次数'] += 1
            dir[i]['图结构平均得分'] += load_dict[i][j]['revised score']
        if load_dict[i][j]["case_type"] == '树结构':
            dir[i]['树结构提交次数'] += 1
            dir[i]['树结构平均得分'] += load_dict[i][j]['revised score']
        if load_dict[i][j]["case_type"] == '数字操作':
            dir[i]['数字操作提交次数'] += 1
            dir[i]['数字操作平均得分'] += load_dict[i][j]['revised score']
        if load_dict[i][j]["case_type"] == '排序算法':
            dir[i]['排序算法提交次数'] += 1
            dir[i]['排序算法平均得分'] += load_dict[i][j]['revised score']
        if load_dict[i][j]["case_type"] == '查找算法':
            dir[i]['查找算法提交次数'] += 1
            dir[i]['查找算法平均得分'] += load_dict[i][j]['revised score']
        if load_dict[i][j]["case_type"] == '数组':
            dir[i]['数组提交次数'] += 1
            dir[i]['数组平均得分'] += load_dict[i][j]['revised score']
        if load_dict[i][j]["case_type"] == '线性表':
            dir[i]['线性表提交次数'] += 1
            dir[i]['线性表平均得分'] += load_dict[i][j]['revised score']

for i in load_dict:  # i为user_id
    if dir[i]['字符串提交次数'] == 0:
        dir[i]['字符串平均得分'] == 0
    else:
        dir[i]['字符串平均得分'] = dir[i]['字符串平均得分'] / dir[i]['字符串提交次数']  # 计算平均值
    if dir[i]['图结构提交次数'] == 0:
        dir[i]['图结构平均得分'] == 0
    else:
        dir[i]['图结构平均得分'] = dir[i]['图结构平均得分'] / dir[i]['图结构提交次数']
    if dir[i]['树结构提交次数'] == 0:
        dir[i]['树结构平均得分'] == 0
    else:
        dir[i]['树结构平均得分'] = dir[i]['树结构平均得分'] / dir[i]['树结构提交次数']
    if dir[i]['数字操作提交次数'] == 0:
        dir[i]['数字操作平均得分'] == 0
    else:
        dir[i]['数字操作平均得分'] = dir[i]['数字操作平均得分'] / dir[i]['数字操作提交次数']

    if dir[i]['排序算法提交次数'] == 0:
        dir[i]['排序算法平均得分'] == 0
    else:
        dir[i]['排序算法平均得分'] = dir[i]['排序算法平均得分'] / dir[i]['排序算法提交次数']

    if dir[i]['查找算法提交次数'] == 0:
        dir[i]['查找算法平均得分'] == 0
    else:
        dir[i]['查找算法平均得分'] = dir[i]['查找算法平均得分'] / dir[i]['查找算法提交次数']

    if dir[i]['数组提交次数'] == 0:
        dir[i]['数组平均得分'] == 0
    else:
        dir[i]['数组平均得分'] = dir[i]['数组平均得分'] / dir[i]['数组提交次数']
    if dir[i]['线性表提交次数'] == 0:
        dir[i]['线性表平均得分'] == 0
    else:
        dir[i]['线性表平均得分'] = dir[i]['线性表平均得分'] / dir[i]['线性表提交次数']

    dir[i]['score'] = [dir[i]['字符串平均得分'], dir[i]['图结构平均得分'], dir[i]['树结构平均得分'], dir[i]['数字操作平均得分'], dir[i]['排序算法平均得分'],
                       dir[i]['查找算法平均得分'], dir[i]['数组平均得分'], dir[i]['线性表平均得分']]

sorted(dir)
print(len(dir))
with open("../data/updated_users_analysis_source.json", 'w', encoding='utf-8') as ans:
    json.dump(dir, ans, ensure_ascii=False, indent=4)
