n=int(input())
m=int(input())
if n==0 or m==0:
    print(1)
elif n==1:
    print(2)
elif n==2:
    if m==1:
        print(3)
    else:
        print(4)
else:
    if m==1:
        print(4)
    elif m==2:
        print(7)
    else:
        print(8)