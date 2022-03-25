# a=[11, 5, 17, 18, 23, 50]
# for i in a:
#     if i%2==0:
#         a.remove(i)
# print(i)

a=[11,5,17,18,23,50,1]
b=[]
i=0
while i<len(a):
    if a[i]%2==0:
        a.remove(a[i])
    i+=1
print(a)

