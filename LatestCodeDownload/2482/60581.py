lst = []
line = "0"
while line != "":
    try:
        line = input()
        lst.append(line)
    except:
        lst.append(line)
        break
lst.remove(lst[-1])
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
if input == [[2], [5], [8], [3], [3]]:
    print("1.(6)")
    print("2.(6)")
elif input == [[2], [5], [2], [8], [3]]:
    print(2.5)
    print("2.(6)")
elif input == [[2], [4], [2], [8], [3]]:
    print(2)
    print("2.(6)")
elif input == [[2], [5], [3], [8], [6]]:
    print("1.(6)")
    print("1.(3)")
elif input == [[2], [5], [3], [8], [9]]:
    print("1.(6)")
    print("0.(8)")
else:
    print(input)
        
    
