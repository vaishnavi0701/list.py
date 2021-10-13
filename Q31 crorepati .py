list=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
i=0
dilwale=0
lakhpati=0
crorepati=0
while i<len(list):
    a=list[i]
    if a<=100000:
        dilwale=dilwale+1
    elif a<=10000000:
        lakhpati=lakhpati+1
    elif a<=1000000000:
        crorepati=crorepati+1
    i=i+1
print(dilwale,"dilwale hai")
print(lakhpati,"lakhpati hai")
print(crorepati,"crorepati hai")