list=['n','i','t','i','n']
i=0
while i<len(list):
    i=i+1
print(list[0:5])
print(list[::-1])
a=list[0:5]
b=list[::-1]
if a==b:
    print("its palindrom")
else:
    print("its not a palindrome")

