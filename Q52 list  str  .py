a=["A1",1,"B2",2,"C1",3,"D4",4]
i=0
b=[]
while i<len(a):
    if type (a[i]==str):
        b.append(a[i])
    i=i+1
print(b)



