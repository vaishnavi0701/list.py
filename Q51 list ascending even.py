
## even value ek jageprrhna chaliye only odd no. ki descending hona chahiye

s=[7,6,5,4,3,2,1]
i=0
b=[]
for i in range(len(s)):
    if s[i]%2==0:
        pass
    else:
        b.append(s[i])
print(b)       
i=0
for i in range(len(b)):
    j=i
    temp=0
    for j in range(len(b)):
        if b[j]>b[i]:
            temp=b[i]
            b[i]=b[j]
            b[j]=temp
i=0
for i in range(len(s)):
    if s[i]%2==0:
        a=s.index(s[i])
        b.insert(a,s[i])
print(b)


