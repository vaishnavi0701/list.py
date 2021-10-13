# list=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# a=0
# b=0
# while i<len(list):
#     if list[i]%2==0:
#         print(list[i],"even number")
#         a=a+list[i]
#     else:
#         print(list[i],"odd number")
#         b=b+list[i]
#     i=i+1
# print("even",a)
# avg=a/4
# print(avg)
# print("odd",b)
# avg=a/7
# print(avg)

i=1
while i<=5:
    num=int(input("Enter the number:"))
    if num==5:
        print("wow , you guessed correct number",("\U0001F642"))
    if num%5==0:
        break
    elif num<5:
        print("Number entered by you entered is small, try one more time","\U0001F612")
    elif num>5:
        print("Number entered by you entered is greater, try one more time ""\U0001F612")
    i+=1
else:
    print("Game Over","\U0001F607")

