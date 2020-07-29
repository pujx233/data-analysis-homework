import json

fp = open("../data/data_all.json", "r", encoding="utf-8")
data = json.load(fp)
fp.close()
for case_id, details in data.items():
    del details["records"]
    details["num_of_isco"] = details["num_of_iscopy"]
    del details["num_of_iscopy"]
    details["average"] = details["score_average"]
    del details["score_average"]
    del details["score_median"]
    del details["score_standard_deviation"]
    del details["case_zip"]

with open("../data/simplified_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
