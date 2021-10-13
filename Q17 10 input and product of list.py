# i=1
# a=[]
# size=int(input("enter no of items"))
# for i in range(size):
#     val=int(input("enter the number"))
#     a.append(val)
#     i=i-1
# product=1
# for i in range(size):
#     product=product*a[i]
# print(product)
    


list=[1,2,3]
i=0
pro=1
while i<len(list):
    pro=pro*list[i]
    i=i+1
print(pro)