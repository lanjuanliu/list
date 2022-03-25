# a=[("z",3),("y",5),("i",1),("j",2),("x",4)]
# i=0
# while i<len(a)-1:
#         if a[i]>a[i+1]:
#                print(a[i],end=" ")
#         i+=1
a=[("c",3),("y",5),("i",1),("j",2),("x",4)]
# i=0
# while i<len(a)-1:
#     j=0
#     while j<len(a[i]):
#         if a[j]>a[j+i]:
#             a[i],a[i+1]=a[i+1],a[i]
#         j+=1
#     i+=1

# print(a) 
# i=0
# while i<len(a):
#     j=0
#     while j<len(a)-1:
#         if a[j+1]>a[i]:
#             a[j],a[j+1]=a[j+1],a[j]
#         j=j+1
#     i+=1
# print(a)


num=int(input("Enter the number"))
a=[]
i=len(str(num))-1
for s in str(num):
    if s!="0":
        a.append(s+"0"*1)
    i-=1
print(" ".join(a))
