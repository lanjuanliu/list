#o/p [[1,2],[2,3],[3,4],[4,5],[5,6]]
a=[1,2,3,4,5,6]
b=[]
i=0
j=i+1
while i<len(a) and j<len(a):
    b1=[]
    b1.append(a[i])
    b1.append(a[j])
    b.append(b1)
    i+=1
    j+=1
print(b)
