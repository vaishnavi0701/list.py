i=1
a=[]
size=int(input("enter no of items"))
for i in range(size):
    value=int(input("enter number"))
    a.append(value)
    i=i-1
print(a)
sum=0
for i in range(size):
    sum=sum+a[i]
print("sum of list",sum)
product=1
for i in range(size):
    product=product*a[i]
print("product of list",product)
max=a[0]
min=a[0]
while i<len(a):
    x=a[i]
    if x>max:
        max=x
    if x<min:
        min=x
    i=i+1
print("maximum value",max)
print("minimum value",min)
# avg=sum//









