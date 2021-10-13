a=[2,312,123,3,12,23,12,12]
i=1
max=a[0]
min=a[0]
while i<len(a):
    f=a[i]
    if f>max:
        max=f
    if f<min:
        min=f
    i=i+1
print(max,"maximum value")
print(min,"minimum value")



        

