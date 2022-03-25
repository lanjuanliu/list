magic_square=[[8,3,4],
             [1,5,9],
             [6,7,2]]
i=0
while i<len(magic_square):
    row=0
    coulum=0
    j=0
    while j<len(magic_square):
        row=row+magic_square[i][j]
        coulum=coulum+magic_square[j][i]
        d=0
        while d<len(magic_square):
            d1=0
            d2=0
            c=0
            while c<len(magic_square):
                d1=d1+magic_square[d][c]
                d2=d2+magic_square[c][d]
                d1=d2
                c=c+1
                
            d=d+1
        j=j+1
    i=i+1
print(row)
print(coulum)
print(row)
print(coulum)
print(d1)
if coulum==row==d1:
    print("it is a magic square")
else:
    print("not a mag") 
