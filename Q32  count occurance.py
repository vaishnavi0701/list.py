list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
i=0
l=[]
while i<len(list):
    j=0
    a=[]
    count=0
    while j<len(list):
        if list[i]==list[j]:
            count=count+1
        j=j+1
    a.append(list[i])
    a.append(count)
    if a not in l:
        l.append(a)
    i=i+1
print(l)


    
