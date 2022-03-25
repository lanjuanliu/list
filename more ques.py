# a=1000
# i=0
# while i<=a:
#     if i%3==0:
#         print("nav")
#     if i%7==0:
#         print("gurukul")
#     if i%21==0:
#         print("navgurukul")
#     i+=1

# a= ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
# b=[]
# i=0
# while i<len(a):
#     if a[i] not  in b:
#         b.append (a[i])
#     i+=1
# print(b)


list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
a=[]
# i=0
# while i<len(list1):
#     j=0
#     while j<len(list2):
#         if list1[i]!=list2[j]:
#             del list1[i]
#             del list2[j]
#         i+=1
#     j+=1
# print(list1)
# print(list2)
            
i=0
while i <len(list1):
    j=0
    while j<len(list2):
        if list1[i]!=list2[j]:
            a.append(list1[i])
            a.append(list2[j])
        i+=1
    j+=1
print(a)
