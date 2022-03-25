a=[1, 2, 2, 5, 8, 4, 4, 8]
# n=[]
# count=0
# for item in a:
#     if item not in n:
#         count += 1
#         n.append(item)
# print("unique list is",count)
        

b=[]
count=0
i=0
while i<len(a):
    if a[i] not in b:
        count+=1
        b.append(a[i])
    i+=1
print("unique list is",count)
