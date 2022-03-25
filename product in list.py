a = [6,1,3,5,6,3,1]
b=[]
c=1
i=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        c=c*b[i]
    i+=1
print(c)
