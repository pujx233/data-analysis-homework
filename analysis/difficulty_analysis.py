import json
import math
import numpy as np
from statistics import mean

upload_times_rate=0.3
upload_intervals=0.1
score_rate=0.5
pass_rate=0.1


#利用离散程度来判断使用平均数还是中位数
def get_score(std,avg,median):
    if std>10:
        return median
    else:
        return avg



def map_difficulty(max,min):
    grade=(max-min)/5
    return [min,min+grade,min+grade*2,min+grade*3,min+grade*4]

def get_grade(grades,data):
    for i in range(0,len(grades)):
        if(data>grades[i]):
            return i+1


def get_difficulty(data):
    for case_id, details in data.items():
        records = details["records"]
        upload_times_ratio=






def main():
    fp = open("../data/data_all.json", "r", encoding="utf8")
    data = json.load(fp)
    fp.close()
    data=get_difficulty(data)
    with open("../data/data_all.json","w") as fp_3:
        json.dump(data,fp_3,indent=4)



if __name__ == '__main__':
    main()


