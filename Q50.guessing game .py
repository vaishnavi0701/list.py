


print("there are 5 chances")
print("you have to enter number from 1 to 10")

i=1
while i<=5:
    num=int(input("Enter the number:"))
    if num==7:
        print("wow , you guessed correct number",("\U0001F642"))
    if num%7==0:
        break
    elif num<7:
        print("Number entered by you is small, try one more time","\U0001F612")
    elif num>7:
        print("Number entered by you is greater, try one more time ""\U0001F612")
    i+=1
else:
    print("Game Over","\U0001F607")





    
