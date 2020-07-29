import json
import time


# return {str} '"%m-%d-%H-%M"'
def timestamp_to_str(timestamp):
    timestamp = int(timestamp * (10 ** (10 - len(str(timestamp)))))
    time_local = time.localtime(timestamp)
    dt = time.strftime("%m-%d-%H-%M", time_local)
    return dt


f = open('../data/test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
data = list(dict.values(data))

# 生成user_time_data.json

out_coffee = {}
for user in data:
    user_id = user["user_id"]
    cases = user["cases"]
    out_coffee[user_id] = {"user_id": user_id}
    for case in cases:
        out_coffee[user_id][case["case_id"]] = []
for user in data:
    user_id = user["user_id"]
    cases = user["cases"]
    for case in cases:
        # user_coffee
        for record in case["upload_records"]:
            out_coffee[user_id][case["case_id"]].append(timestamp_to_str(record["upload_time"]))
        # user_time_data

json_out = json.dumps(out_coffee, ensure_ascii=False, indent=2)
with open('user_coffee.json', 'w') as f:
    f.write(json_out)
