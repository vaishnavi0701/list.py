i=1
a=[]
size=int(input("enter no of items"))
for i in range(size):
    val=int(input("enter number"))
    a.append(val)
    i=i-1
sum=0
for i in range(size):
    sum=sum+a[i]
print([sum])





