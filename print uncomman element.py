lst1 = [ [1, 2], [3, 4], [5, 6] ]
lst2 = [ [3, 4], [5, 7], [1, 2] ]
i=0
while i<len(lst1):
    j=0
    while j<len(lst2):
        if lst1[i]!=lst2[j]:
            del lst1[i]
            del lst2[j]
        j+=1
    i+=1
print(lst1)
print(lst2)


