num=input()
nums=[]
dick={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
for i in num:
    if i in"1234567890":
        nums.append(dick[i])
print(sorted(nums))
