numbers=[50,40,23,70,56,12,5,10,7]
i=0
p=[]
count=0
while i<len(numbers):
    m=numbers[i]
    if m>20 and m<40:
        p.append(m)
        count=count+1
    i=i+1
print(p,count)




