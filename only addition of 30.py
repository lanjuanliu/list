lst=[13,17,15,15,12,11]
x=[]
i=0
while i<len(lst):
    j=i+1
    while j<len(lst):
        if lst[j]+lst[i]==30:
            x.append (lst[i])
            x.append(lst[j])
        j+=1
    i+=1
print(x)