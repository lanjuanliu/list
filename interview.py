# a=[1,2,3,4,5,6,7]
# i=0
# while i<len(a):
#     reverse=(a[::-1])
#     i+=1
# print(reverse)


# a=input("enter the number")
# i=0
# while i<len(a):
#     b=(a[::-1])
#     i+=1
# print(b)


list1=[13,17,15,15,12,11]
x=[]
i=0
while i<len(list1):
    j=i+1
    while j<len(list1):
        if list1[i]+list1[j]==30:
           x.append(list1[i])
           x.append(list1[j])
        j+=1
    i+=1
print(x)
