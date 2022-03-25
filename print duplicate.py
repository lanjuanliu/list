a=[1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9] 
# b=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# print(b)
b=[]
i=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
print(b)