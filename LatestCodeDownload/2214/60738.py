a=input().split("+")
b=input().split("+")
a_r=int(a[0])
a_i=int(a[1][:-1])
b_r=int(b[0])
b_i=int(b[1][:-1])
r=0
i=0
i1=a_i*b_r+a_r*b_i
r1=a_r*b_r-a_i*b_i
print(str(r1)+"+"+str(i1)+"i")
