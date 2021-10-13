magic_square=[[8,3,4],
              [1,5,9],
              [6,7,2]]
i=0
s=0
while i<len(magic_square):
    col=0
    while col<len(magic_square):
        s=s+magic_square[i][col]
        col=col+1
    i=i+1
print(s)
j=0
s1=0
while j<len(magic_square):
    row=0
    while row<len(magic_square):
        s1=s1+magic_square[j][row]
        row=row+1
    j=j+1
print(s1)
k=0
s2=0
while k<len(magic_square):
    dig=0
    while dig<len(magic_square):
        s2=s2+magic_square[k][dig]
        dig=dig+1
    k=k+1
print(s2)
if s==s1==s2:
    print(" it is magic square")
else:
    print("it is not a magic square")