 
mainstr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
l=mainstr.split()
i=0
while i<len(l):
    if l[i]=="over":
        i=i+1
    print(l[i],end=" ")
    i=i+1