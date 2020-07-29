import json

f = open('calendar_heat_map.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
num = 0
new_num = 0
judge = False

for i in data:
    m = data[i]
    for j in m:
        print(j)
        if len(j) != 10:
            break
        num += m[j]
        if j == '2020-03-25':
            print("add new_num")
            new_num += m[j]
            judge = True
        if judge:
            new_num += m[j]
    data[i]["提交总数"] = num
    data[i]["临时抱佛脚提交"] = new_num
    if num == 0:
        data[i]["临时抱佛脚占比"] = None
    else:
        data[i]["临时抱佛脚占比"] = round(new_num / num, 2)
    num = 0
    new_num = 0
    judge = False

with open("calendar_heat_map.json", 'w', encoding='utf-8') as ans:
    json.dump(data, ans, ensure_ascii=False, indent=4)


