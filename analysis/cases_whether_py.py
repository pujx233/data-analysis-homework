def whether_py(fname):
    with open(fname, encoding='utf-8') as data:
        for file_line in data.readlines():
            if file_line.startswith('#include'):
                return False
            if file_line!=" ":
                lst=list(file_line)
                for i in range(0,len(lst)-1):
                    if lst[i]=='/' and lst[i+1]=='/':
                        return False
    return True


if __name__ == '__main__':
    filename = "../LatestCodeDownload/3544_2172.py"
    res=whether_py(filename)
    print('是否为python语言：  %s' % res)

