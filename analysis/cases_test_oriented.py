def whether_test_oriented(fname):
    with open(fname, encoding='utf-8') as data:
        code_counts=0  #有效代码行数
        nums=0 #以print开头的代码行数
        for file_line in data.readlines():
            if not file_line.startswith('#'): #过滤注释行
                if file_line!=" ": #过滤空行
                    code_counts += 1
                    if file_line.startswith('print'):
                        nums+=1
        if code_counts!=0 and nums/code_counts>0.3: #print语句占总语句的30%以上，判定为面向用例编程（系数待定）
            return True

    return False


if __name__ == '__main__':
    filename = "../LatestCodeDownload/3544_2172.py"
    res = whether_test_oriented(filename)
    print('是否面向用例编程：  %s' % res)

