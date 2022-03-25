num=[1,2,3,[4,5],[6,7,8,],9,10]
i=0
a=[]
while i<len(num):
    if type(num[i])==type([]):
        j=0
        while j<len(num[i]):
            if type (num[i][j])==type([]):
                k=0
                while k<len(num[i][j]):
                    a.append(num[i][j][k])
                    k+=1
            else:
                a.append(num[i][j])
            j+=1
    else:
        a.append(num[i])
    i+=1
print(a)