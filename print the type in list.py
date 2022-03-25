# a=[1,1.5,True,"A",[1,2]]
# i=0
# while i<len(a):
#     print(type(a[i]))
#     i+=1


# a=[7,9,6,4,11,13]
# b=[]
# i=0
# while i<len(a):
#     if a[i]==11:
#       b.append(a[i])ia
#     if a[i]==13:
#       b.append(a[i])
#     i+=1
# print(b)


a=["A","B","c","D"] 
b=[]
n=2
i=1
while i<=n:
    j=0
    while j<len(a):
        c=a[j]+str(i)
        b.append(c)
        j+=1
    i+=1
print(b)


# a=["A","B","C","D"]
# b=[]
# n=2
# i=0
# while i<n:
#     c=a[i]+str(i)
#     b.append(c)
#     i+=1
# print(b)



