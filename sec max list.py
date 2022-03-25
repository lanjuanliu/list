lst=[1,2,-3,4,-7]
i=0
while i<len(lst):
    j=0
    while j<len(lst):
        if lst[i]<lst[j]:
            b=lst[i]
            lst[i]=lst[j]
            lst[j]=b
        j+=1
    i+=1
print(b)