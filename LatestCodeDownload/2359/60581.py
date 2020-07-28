import sys

lst = []
for line in sys.stdin:
    if line.strip()=="":
        break
    lst.append(line)

input = []
#读入处理
for i in range(0,len(lst)):
    theLine = []
    j = 0
    while j < len(lst[i]):
        str = ''
        judgeWord = False
        judgeNumber = False
        if lst[i][j]>='A' and lst[i][j]<='Z':
            judgeWord = True
            str += lst[i][j]
        while judgeWord:
            j += 1
            if j == len(lst[i]):
                theLine.append(str)
                break
            if lst[i][j]>='A' and lst[i][j]<='Z':
                str += lst[i][j]
            else:
                judgeWord = False
                theLine.append(str)

        if lst[i][j]>='0' and lst[i][j]<='9':
            judgeNumber = True
            str += lst[i][j]
        while judgeNumber:
            j += 1
            if j == len(lst[i]):
                theLine.append(int(str))
                break
            if lst[i][j]>='0' and lst[i][j]<='9':
                str += lst[i][j]
            else:
                judgeNumber = False
                theLine.append(int(str))
        j += 1
    input.append(theLine)

testNumber = input[0][0]

start = 1
count = 0
while count < testNumber:
    numbers = input[start][0]
    numberList = input[start+1].copy()
    numberList.sort()
    numberList.reverse()
    zooms = 0
    for i in range(numbers-1):
        for j in range(i+1,numbers):
            if numberList.count(numberList[i]-numberList[j]):
                if numberList[i] != 2*numberList[j] or numberList.count(numberList[i]-numberList[j])>1:
                    zooms += 1
                
    zooms = int(zooms/2)
    if zooms==0:
        print("-1")
    else:
        print(zooms)

    start += 2
    count += 1