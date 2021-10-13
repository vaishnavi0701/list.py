a = [1,1,2,2,3,3]
i=0
pro=1
while i<len(a):
    j=0
    while j<len(a):
        if a[i]==a[j]:
            del(a[j])
            pro=pro*a[i]
        j=j+1
    i=i+1
print(a)
print(pro)



