list=[23,14,56,12,19,9,15,25,31,42,43]
i=0
a=0
b=0
while i<len(list):
    if list[i]%2==0:
        print(list[i],"even number")
        a=a+list[i]
    else:
        print(list[i],"odd number")
        b=b+list[i]
    i=i+1
print("even:",a)
avg=a/4
print(avg)
print("odd:",b)
avg=a/7
print(avg)


