temp=input().split(',')
b=map(eval,temp)
list1=list(b)
c=eval(input())
if(c in list1):
    print(list1.index(c))
else:
    list1.append(c)
    list1.sort()
    print(list1.index(c))