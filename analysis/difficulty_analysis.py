import json
import math
import numpy as np
import pandas as pd
from statistics import mean

upload_times_rate = 0.5
# upload_intervals=0.1
score_rate = 0.3
pass_rate = 0.2


def get_grades(max, min, data):
    grades = {}
    for key in data.keys():
        grade = 1 + (5 - 1) / (max - min) * (data[key] - min)
        grades[key] = grade

    return grades

def get_grades_2(max,min,data):
    grades = {}
    for key in data.keys():
        grade =5 - (5 - 1) / (max - min) * (data[key] - min)
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
    scores_grades = get_grades_2(np.max(list(scores.values())), np.min(list(scores.values())), scores)
    passes_grades = get_grades_2(np.max(list(passes.values())), np.min(list(passes.values())), passes)

    for case_id, details in data.items():
        records = details["records"]
        if(upload_times_grades[case_id]>=4.8 or scores_grades[case_id]>=4.8 or passes_grades[case_id]>=4.8):
            difficulty=5
        else:
            difficulty = round((upload_times_grades[case_id] * upload_times_rate + scores_grades[case_id] * score_rate +
                            passes_grades[case_id] * pass_rate) * 10) / 10
            if(difficulty>1.15 and difficulty<1.7):
                difficulty=2.0
            elif(difficulty>=1.7 and difficulty<2.45):
                difficulty=3.0
            elif (difficulty >= 2.45 and difficulty < 3.3):
                difficulty = 4.0
            elif (difficulty >= 3.3 and difficulty <=5):
                difficulty = 5.0
        print(round(difficulty))

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
