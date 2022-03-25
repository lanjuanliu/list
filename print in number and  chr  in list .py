a=["A","B","C"]
b=[]
c=2
i=1
while i<=c:
    j=0
    while i<len(a):
        c=a[j]+str(i)
        b.append(c)
        j+=1
    i+=1
print(b)