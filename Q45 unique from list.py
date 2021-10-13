a = [1, 2, 2, 5, 8, 4, 4, 8]
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        if a[i]==a[j]:
            del(a[j])
        j=j+1
    i=i+1
print(a)

    


