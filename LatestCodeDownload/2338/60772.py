import sys

def sum(arr,N,X):
    for i in range(0,N):
        for j in range(i+1,N):
            if arr[i]+arr[j] == X:
                return "Yes"
    return "No"

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0,int(test)):
    info = Input[begin].split()
    N = int(info[0])
    X = int(info[1])
    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))
    begin += 2
    print(sum(arr,N,X))
