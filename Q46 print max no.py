
numbers=[1,2,3,4,5,6,7,8,9,11,13,15,30]
i=0
b=numbers[0]
while i<len(numbers):
    if numbers[i]>b:
        b=numbers[i]
    i=i+1
print(b)
    