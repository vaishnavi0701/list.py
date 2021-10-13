z=input("enter any word ")
i=0
b=[]
while i<len(z):
    b.append(z[i])
    i+=1
print(b)
j=0
c=[]
while j<len(b):
    if b[j]=="a" or b[j]=="e" or b[j]=="i" or b[j]=="o" or b[j]=="u":
        c.append(b[j])
    j=j+1
print(c)