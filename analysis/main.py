import codeSimilarity.similarity_check as sc
import analysis.detect_analysis as da
import analysis.extra_analysis as ea
import analysis.difficulty_analysis as diff_a


#生成data_all.json文件


if __name__ == '__main__':
    #过滤test_data.json文件并生成具有判断面向用例,判断非python文件,判断非答案记录的json文件
    da.main()

    #将抄袭代码的情况写入data_all.json文件中
    sc.main()

    #将代码有效情况写入data_all.json文件中
    ea.analysis_valid()

    #将有效代码的分数统计情况写入data_all.json文件中
    ea.analysis_score()

    #将难度情况写入data_all.json文件中
    diff_a.main()

