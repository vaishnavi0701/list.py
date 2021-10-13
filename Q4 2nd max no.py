# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
# a=[]
# b=int(input("enter number of elements"))
# for i in range(1,b+1):
#     c=input("enter number of list")
#     a.append(c)
# a.sort()
# print("2nd highest no is",a[b-2])



number=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
i=0
while i<len(number):
    l=number[i]
    if l>number[0] and l<number[3]:
        print("second max",l) 
    i=i+1