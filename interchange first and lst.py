a=[]
n=int(input("enter the number"))
for i in range(0,n):
    element=int(input("enter the number"+str(i+1)+":"))
    a.append(element)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print(a)


# a=[14,19,2,8,23,7,15,4,1]
# i=0
# while i<len(a):
#     a[0],a[-1]=a[-1],a[0]
#     i+=1
# print(a)





