n,m=map(int,input().split())
a=map(int,input().split())
b=map(int,input().split())
a1=[i%2 for i in a].count(1)
b1=[j%2 for j in b].count(1)
result=min(a1,m-b1)+min(b1,n-a1)
print(result)