import json
import pandas as pd


def analysis_valid():
    fp = open("../data/data_all.json", "r", encoding="utf8")
    data = json.load(fp)
    fp.close()

    for key in data.keys():
        num_of_isvalid = 0
        for index, item in enumerate(data[key]["records"]):
            is_valid = True
            if "is_cpp" in item.keys():
                if item["is_cpp"] == True:
                    is_valid = False
            elif "is_case-oriented" in item.keys():
                if item["is_case-oriented"] == True:
                    is_valid = False
            elif "is_answer" in item.keys():
                if item["is_answer"] == True:
                    is_valid = False
            elif "is_copy" in item.keys():
                if item["is_copy"] == True:
                    is_valid = False
            data[key]["records"][index]["is_valid"] = is_valid
            if is_valid:
                num_of_isvalid += 1
        data[key]["num_of_isvalid"] = num_of_isvalid

    with open("../data/data_all.json", "w") as fp_3:
        json.dump(data, fp_3, indent=4)


def analysis_score():
    fp = open("../data/data_all.json", "r", encoding="utf8")
    data = json.load(fp)
    fp.close()

    for case_id, details in data.items():
        records = details["records"]
        final_scores = []
        for record in records:
            if (record["is_valid"] == True):
                final_scores.append(record["final_score"])

        grades = pd.Series(final_scores)
        details["score_average"] = grades.mean()  # 平均值
        details["score_median"] = grades.median()  # 中位数
        details["score_standard_deviation"] = grades.std()  # 标准差
        details["user_count"] = len(records)  # 做题人数
        details["num_of_full-score"] = int(grades.value_counts()[100])  # 计算满分人数

        details["pass_rate"] = details["num_of_full-score"] / details["num_of_isvalid"]

    with open("../data/data_all.json", "w") as fp_3:
        json.dump(data, fp_3, indent=4)


if __name__ == '__main__':
    analysis_valid()
    analysis_score()
