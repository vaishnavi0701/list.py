i=4
a=[]
while i>=0:
    num=input("enter number") 
    a.append(num)
    i=i-1
print(a)
j=0
while i<len(a):
    i=i+1
print(a[0:5])
print(a[::-1])
x=a[0:5]
y=a[::-1]
if x==y:
    print("same")
else:
    print("not same")
