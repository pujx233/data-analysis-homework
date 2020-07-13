
def num_of_rows(fname):
    with open(fname, encoding='utf-8') as data:
        code_counts=0  #代码行数
        annotation_counts = 0  # 注释行数
        for file_line in data.readlines():
            # 统计注释行(一行中只有注释)
            if file_line.startswith('#'):
                annotation_counts += 1
            # 统计代码行
            elif file_line!=" ": #过滤空行
                code_counts += 1
    # 返回代码行数，注释行数
    return code_counts, annotation_counts


if __name__ == '__main__':
    filename = "../LatestCodeDownload/3544_2172.py"
    code_counts, annotation_counts = num_of_rows(filename)
    print('代码总行数为：  %s' % code_counts)
    print('注释行总行数为： %s' % annotation_counts)
