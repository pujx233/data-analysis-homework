import json

# 更新updated Database of Mooctest.json

fp = open("../data/updatedDatabase of Mooctest.json", "r", encoding="utf8")
data = json.load(fp)
fp.close()
fp_2 = open("../data/exercise_cheat_users.json", "r", encoding="utf8")
data_users = json.load(fp_2)
fp_2.close()
for key in data.keys():
    for index, item in enumerate(data[key]["records"]):
        if (key in data_users.keys()):
            if (item["user_id"] in data_users[key]["user_id"]):
                data[key]["records"][index]["is_copy"] = True
            else:
                data[key]["records"][index]["is_copy"] = False
        else:
            data[key]["records"][index]["is_copy"] = False

with open("../data/updatedDatabase of Mooctest.json", "w") as fp_3:
    json.dump(data, fp_3, indent=4)