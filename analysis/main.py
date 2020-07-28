import codeSimilarity.similarity_check as sc
import analysis.detect_analysis as da
import analysis.extra_analysis as ea
import analysis.difficulty_analysis as diff_a
import json
# 生成data_all.json文件



if __name__ == '__main__':
    # 过滤test_data.json文件并生成具有判断面向用例,判断非python文件,判断非答案记录的json文件
    da.main()

    # 将抄袭代码的情况写入data_all.json文件中
    sc.main()

    # 将代码有效情况写入data_all.json文件中
    ea.analysis_valid()

    # 将有效代码的分数统计情况写入data_all.json文件中
    ea.analysis_score()

    # 将难度情况写入data_all.json文件中
    diff_a.main()

    with open('../data/updatedDatabase of Mooctest.json', encoding='utf-8') as f:
        data = json.loads(f.read())
        for case_id, details in data.items():
            for name in ["case_zip", "records", "num_of_testCases", "group", "median", "std"]:
                del details[name]
    save_as_file(data, "../data/simplifiedDatabase of Mooctest.json")
