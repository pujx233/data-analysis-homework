import json
import math
import numpy as np
import pandas as pd
from statistics import mean

upload_times_rate = 0.3
# upload_intervals=0.1
score_rate = 0.6
pass_rate = 0.1


def get_grades(max, min, data):
    grades = {}
    for key in data.keys():
        grade = 1 + (5 - 1) / (max - min) * (data[key] - min)
        print(grade)
        grades[key] = grade
    return grades


def get_difficulty(data):
    upload_times = {}
    intervals = {}
    scores = {}
    passes = {}

    for case_id, details in data.items():
        records = details["records"]
        upload_times[case_id] = details["total_upload_times"]
        scores[case_id] = details["score_average"]
        passes[case_id] = details["pass_rate"]

    upload_times_grades = get_grades(np.max(list(upload_times.values())), np.min(list(upload_times.values())),
                                     upload_times)
    scores_grades = get_grades(np.max(list(scores.values())), np.min(list(scores.values())), scores)
    passes_grades = get_grades(np.max(list(passes.values())), np.min(list(passes.values())), passes)

    for case_id, details in data.items():
        records = details["records"]
        difficulty = round((upload_times_grades[case_id] * upload_times_rate + scores_grades[case_id] * score_rate *
                            passes_grades[case_id] * pass_rate) * 10) / 10
        details["difficulty"] = int(round(difficulty))

    return data


def main():
    fp = open("../data/data_all.json", "r", encoding="utf-8")
    data = json.load(fp)
    fp.close()
    data = get_difficulty(data)
    with open("../data/data_all.json", "w", encoding="utf-8") as fp_3:
        json.dump(data, fp_3, ensure_ascii=False,indent=4)


if __name__ == '__main__':
    main()
