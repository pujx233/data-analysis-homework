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
    details['final'] = [details['difficulty'] * 20, 100 * ( details['num_of_iscpp'] / details["user_count"]),
                        100 * ( details['num_of_is_case-oriented'] / details["user_count"]), details['average'],
                        100 * details["num_of_valid_full-score"] / details["user_count"],100*details["num_of_isco"]/details["user_count"],100*details[ "pass_rate"]]


with open("../data/simplified_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
