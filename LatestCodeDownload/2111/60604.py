a=int(input())
def ope(a):
    if a==1 or a==2 or a==3 or a==4:
        return True
    else:
        if a%2==0: 
            return ope(a/2)
        elif a%3==0:
            return ope(a/3)
        elif a%5==0:
            return ope(a/5)
        else:return False
i=1
while(a>0):
    if ope(i):
        
        a-=1
        i+=1
    else:
        i+=1
print(i-1)