import analysis.detect_functions as df
import pandas as pd
import json


def detect(data):
    
    new_data = {}
    count = 0
    for user_id, details in data.items():
        cases = details['cases']
        for case in cases:
            if case["case_id"] not in new_data.keys():
                new_data[case["case_id"]] = {"case_id": case['case_id'],
                                             "case_type": case["case_type"],
                                             "case_zip": case["case_zip"],
                                             "records": []
                                             }
            new_data[case["case_id"]]["records"].append({"user_id": user_id,
                                                         "final_score": case["final_score"],
                                                         "upload_times": len(case["upload_records"]),
                                                         "upload_records": case["upload_records"]
                                                         })
        count += 1
    return analyse(new_data)

def analyse(data: list):

    for case_id, details in data.items():
        records = details["records"]

        # 剔除upload_records为空的数据（异常）
        i = 0
        while i < len(records):
            if records[i]["upload_times"] == 0:
                print(case_id, "  ", records[i])
                del records[i]
                i -= 1
            else:
                try:
                    final_record = records[i]["upload_records"][-1]
                    records[i]["final_upload_id"] = final_record["upload_id"]
                    records[i]["final_code_url"] = final_record["code_url"]
                except Exception as e:
                    print(case_id, "  ", records[i])
                    print(e)
            i += 1

        data[case_id]["total_upload_times"] = sum([record["upload_times"] for record in records])
        data[case_id]["user_count"] = len(records)


        # 检测代码行数 & 面向用例情况 & 是否为python
        num_of_iscpp = 0  # 非python计数
        num_of_isco = 0  # 面向用例计数
        num_of_isanswer = 0  # 与答案一致计数
        for record in records:
            user_id = record["user_id"]
            upload_id = str(record["final_upload_id"])
            answerpath = '../TestDownload//' + case_id + "//.mooctest//answer.py"
            codepath = '../LatestCodeDownload//' + case_id + "//" + user_id + ".py"

            try:
                record["num_of_line"] = 0
                record["is_cpp"] = True
                record["is_case-oriented"] = True
                record["is_answer"] = True

                # 代码行数
                lst = df.num_of_rows(codepath)
                record["num_of_line"] = lst

                if record["num_of_line"] > 0:
                    # 检测是否为答案
                    flag_answer = df.detect_is_answer(answerpath, codepath)
                    record["is_answer"] = flag_answer
                    if flag_answer:
                        num_of_isanswer += 1

                    # 检测是否为cpp代码
                    flag_cpp = df.detect_no_py(codepath)
                    record["is_cpp"] = flag_cpp
                    if flag_cpp:
                        num_of_iscpp += 1

                    # 面向用例情况
                    flag_co = df.detect_case_oriented(codepath)
                    record["is_case-oriented"] = flag_co
                    if flag_cpp == False and flag_co == True:
                        num_of_isco += 1


            except Exception as e:
                print(e)
                continue
        for record in records:
            del record["upload_records"]

        # 记录面向用例、非python情况
        data[case_id]["num_of_isanswer"] = num_of_isanswer
        data[case_id]["num_of_iscpp"] = num_of_iscpp
        data[case_id]["num_of_is_case-oriented"] = num_of_isco


    return data

def main():
    with open('../data/test_data.json',"r", encoding='utf-8') as f:
        data = json.loads(f.read())
        data=detect(data)
        with open("../data/data_all.json", 'w', encoding='utf-8')as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
