a=["A","B","C","D"]
b=[]
x=2
i=1
while i<=x:
    j=0
    while j<len(a):
        c=a[i]+str(i)
        b.append(c)
        j+=1
    i+=1
print(b)