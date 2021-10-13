a=[1,2,"v",3,"a",4,"i",5,"s","h",6]
i=0
b=[]
while i<len(a):
    if type (a[i])==str:
        b.append(a[i])
    i=i+1
print(b)
