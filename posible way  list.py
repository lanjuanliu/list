# List1 = [1998, 2002]
# List2 = [2014, 2016]
# print((List1+List2)*2)

a=[0,9,5]
i=0
while i<len(a):
    j=0
    while j<len(a):
        k=0
        while k<len(a):
            if (i!=j and j!=k and k!=i):
                print(a[i],a[j],a[k])
            k+=1
        j+=1
    i+=1

