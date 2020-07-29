import json
import matplotlib.pylab as pyl


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
    new_data[i]["抄袭占比"] = 0
for j in data_list:
    new_data[j]["抄袭占比"] = data_list[j]["total"] / 200

save_as_file(new_data, 'correlation.json')

f = open('correlation.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

x = []
y = []

for i in data:
    if data[i]["临时抱佛脚占比"] != None and data[i]["抄袭占比"] != 0.0:
        x.append(data[i]["临时抱佛脚占比"])
        y.append(data[i]["抄袭占比"])
print(x)
print(len(x))
print(y)
print(len(y))

pyl.plot(x, y, 'o')
fig = pyl.figure(figsize=(10, 8), dpi=300)  # 设置画布大小，像素

ax1 = fig.add_subplot(1, 1, 1)
# 设置标题
ax1.set_title('the Correlation about Copy and Learning before DDL ')
# 设置横坐标名称
ax1.set_xlabel('Ratio of Doing before DDL')
# 设置纵坐标名称
ax1.set_ylabel('Cheat or Copy')


pyl.scatter(x, y, label='scatter figure')  # 画散点图并指定图片标签
pyl.legend()  # 显示图片中的标签

pyl.savefig(r"../../images/time&cheat.png", dpi=300)
pyl.show()