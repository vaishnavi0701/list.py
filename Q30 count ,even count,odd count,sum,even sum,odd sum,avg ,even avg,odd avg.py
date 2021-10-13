list=[1,2,3,4,5,6,7,8,9,1]
i=0
a=[]
s=[]
even=0
odd=0
sum=0
even_sum=0
odd_sum=0
avg=0
even_avg=0
odd_avg=0
while i<len(list):
    j=list[i]
    if j%2==0:
        a.append(j)
        even=even+1
        even_sum=even_sum+j
        even_avg=even_avg+j
    else:
        s.append(j)
        odd=odd+1
        odd_sum=odd_sum+j
        odd_avg=odd_avg+j
    i=i+1
print(list)
print(a,"even number",even)
print(s,"odd number",odd)
print(even_sum,"even sum")
print(odd_sum,"odd sum")
even_avg=even_sum/even
print(even_avg,"even average")
odd_avg=odd_sum/odd
print(odd_avg,"odd average")

