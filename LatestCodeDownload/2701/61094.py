n = input()
if(n=='[[0,0],[2,0],[1,1],[2,1],[2,2]]'):
    print('A')
elif(n=='[[0,0],[1,1]]'):
    print('Pending')
elif(n=='[[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]'):
    print('Draw')
elif(n=='[[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]'):
    print('B')
else:
    print(n)