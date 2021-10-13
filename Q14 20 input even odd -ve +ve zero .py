i=20
a=[]
while i<0:
    num=input("enter number")
    a.append.num
    i=i-1
odd=0
even=0
zero=0
negative=0
positive=0
i=19
while i>=0:
    if a==0:
        print("zero")
        zero=zero+1
    elif a>0:
        print("positive")
        positive=positive+1
        if a[i]%2==0:
            print("even")
            even=even+1
        else:
            print("odd")
            odd=odd+1
    else:
        print("negative")
        negative=negative+1
        if a%2==0:
            print("even")
            even=even+1
        else:
            print("odd")
            odd=odd+1
    i=i-1


