a = [[4, 1, 6], [7, 8], [4, 10, 8]]
b=[]
i=0
while i<len(a):
    if a[i]:
        a[i].reverse()
    i+=1
print(a)
