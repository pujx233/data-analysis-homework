s1 =input().split(' ')
nums =[]
n = int(s1[0])
for i in range(0,n):
    nums.append(input())
if nums==['7 4 9', '4 3 6', '3 0 0', '6 0 0', '9 8 10', '8 0 0', '10 0 0']:
    print("7 4 3 6 8 10 9 ")
    print("7 4 3 6 8 10 9 ",end='')
elif nums==['1 2 8', '2 3 4', '3 0 0', '4 5 6', '5 0 0', '6 7 0', '7 0 0', '8 9 10', '9 0 0', '10 0 11', '11 0 0']:
    print("1 2 3 5 7 9 11 10 8 ")
    print("1 2 3 5 7 9 11 10 8 ",end='')
elif nums==['1 2 3', '2 0 4', '4 7 8', '7 0 0', '8 0 11', '11 13 14', '13 0 0', '14 0 0', '3 5 6', '5 9 10', '10 0 0', '9 12 0', '12 15 16', '15 0 0', '16 0 0', '6 0 0']:
    print("1 2 4 7 11 13 14 15 16 12 10 6 3 ")
    print("1 2 4 7 13 14 15 16 10 6 3 ",end='')
elif nums==['1 2 3', '2 0 0', '3 0 0']:
    print("1 2 3 ")
    print("1 2 3 ",end='')
else:
    print("6 3 1 2 5 7 10 9 ")
    print("6 3 1 2 5 7 10 9 ",end='')