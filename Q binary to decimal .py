# binary_number=[1, 0, 0, 1, 1,0,1,1,]
# i=0
# count=0
# while i< len(binary_number):
#     count=count+2**2*1-0*binary_number[-i-1]
#     i=i+1
# print(count)


# s=[1,2,3,4,5,6,7]
# d=0
# for  i in s:
#     d=d+1
# print(d)


# num=[50,40,23,70,56,12,5,10,7]
# i=0
# count=0
# t=[]
# while i<len(num):
#     s=num[i]
#     if s>20 and s<40:
#         t.append(s)
#         count=count+1
        
#     i=i+1
# print(t,count)


# num=[50,40,23,70,56,12,5,10,7]
# i=0
# a=num[0]
# while i<len(num):
#     if num[i]>a:
#         a=num[i]
#     i=i+1
# print(a)


# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# i=0
# while i<len(places):
#     i=i+1
# print(places[::-1])

# list=['n','i','t','i','n']
# i=0
# while i<len(list):
#     i=i+1
# print(list[0:5])
# print(list[::-1])
# a=list[0:5]
# b=list[::-1]
# if a==b:
#     print("palindrome")
# else:
#     print("not")


# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7] 
# i=0
# s=[]
# while i<len(list1):
#     if list1[i] not in list2:
#         s.append(list1[i])
#     i=i+1
# print(s)



# list1=[1,342,75,23,98]
# list2=[75,23,98,12,78,10,1]
# i=0
# r=[]
# while i<len(list1):
#     if list1[i] in list2:
#         r.append(list1[i])
#     i=i+1
# print(r)

# i=5
# s=[]
# while i>0:
#     num=int(input("enter no:"))
#     s.append(num)
#     i=i-1
# print(s)


# i=5
# s=[]
# while i>0:
#     num=int(input("enter nu:"))
#     s.append(num)
#     i=i-1
# print(s)
# print(s[::-1])


# i=0
# s=[]
# num=int(input("no of items"))
# for i in range(num):
#     val=int(input("enter elements"))
#     s.append(val)
#     i=i-1
# print(s)
# sum=0
# for i in range(num):
#     sum=sum+s[i]
# print(sum)


# i=0
# s=[]
# num=int(input("no of items"))
# for i in range(num):
#     val=int(input("enter items"))
#     s.append(val)
#     i=i-1
# print(s)
# pro=1
# for i in range(num):
#     pro=pro*s[i]
# print(pro)



# a=[[1,2,3],[4,5,6]]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         print(a[i][j])
#         j=j+1
#     i=i+1






# import json

# dict={"name":"vaishu","age":20,"class":12}
# print(type(dict))
# data=json.dumps(dict)
# print(data)
# print(type(data))


# data1=json.loads(data)
# print(data1)





dic={"a":2,"b":3,"c":{"d":3,"e":5,"f":{"g":8,"h":10}}}
sum=0
for i in dic.values():
    if type(i)==dict:
        for j in i.values():
            if type(j)==dict:
                for k in j.values():
                    sum=sum+k
            else:
                sum=sum+j
    else:
        sum=sum+i
print(sum)






