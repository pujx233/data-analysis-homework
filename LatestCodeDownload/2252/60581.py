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
        if (lst[i][j]>='A' and lst[i][j]<='Z') or (lst[i][j]>='a' and lst[i][j]<='z'):
            judgeWord = True
            str += lst[i][j]
            theLine.append(str.lower())

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
    sectence = input[start].copy()
    word = input[start+1].copy()
    word.sort()
    times = 0
    for i in range(0,len(sectence)-len(word)+1):
        if word.count(sectence[i]):
            subString = sectence[i:i+len(word)].copy()
            subString.sort()
            judge = True
            for i in range(len(word)):
                if subString[i]!=word[i]:
                    judge = False
            if judge:
                times += 1
    print(times)
    start += 2
    count += 1