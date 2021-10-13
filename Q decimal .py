a=[1,1,2,3,4,4,5,1]
# binary=[1,0,0,1,1,0,1,1]
i=0
sum=0
while i<len(a):
    num=a[-i-1]
    sum=sum+num*(2**i)
    i=i+1
print(sum)