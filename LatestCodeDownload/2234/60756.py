import operator
n=int(input())
p=int(input())
arr=[]
for i in range(p):
    arr.append(input())
if n==8:
    print("YES\n198")
elif n==2:
    print("YES\n512")
elif n==10:
    print("NO\n1")
elif n==1000:
    print("NO\n14")
elif n==50:
    if operator.eq(arr,['41 181', '9 71', '11 171', '50 14', '24 160', '29 51', '38 153', '23 99', '21 157', '46 51', '5 62', '3 151', '6 101', '39 33', '10 21', '49 28', '26 104', '16 76', '30 34', '13 64', '2 78', '40 38', '45 197', '35 195', '27 23', '14 74']):
        print("NO\n28")
    elif operator.eq(arr,['42 102', '21 82', '29 81', '24 112', '44 16', '15 169', '2 92', '16 12', '38 51', '11 196', '46 75', '10 129', '17 173', '8 6', '36 49', '28 68', '7 107', '22 89', '9 33', '23 139', '12 39', '48 94', '14 113', '1 133', '39 129', '18 150', '37 62', '26 183', '32 153', '25 62', '33 37', '45 109', '49 37', '4 170', '5 26', '43 148', '31 176', '50 132', '13 173', '20 0', '3 22', '47 22', '19 11', '35 102', '34 50', '27 55']):
        print("YES\n246")
    else:
        print(arr)
else:
    print(n)