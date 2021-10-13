
list= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
a=[]
s=[]
even=0
odd=0
while i<len(list):
    j=list[i]
    if j%2==0:
        a.append(j)
        even=even+1
    else:
        s.append(j)
        odd=odd+1
    i=i+1
print(list)
print(a,"even number",even)
print(s,"odd number",odd)