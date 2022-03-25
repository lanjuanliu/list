# list = [10, 11, 12, 13, 14, 17, 18, 19]
# n=len(list)
# sum=30
# for i in range (0,n):
#     for j in range (i+1,n):
#         if (list[i]+list[j]==sum):
#             print(list[i],",",list[j])


list = [10, 11, 12, 13, 14, 17, 18, 19]
n=len(list)
sum=30
i=0
while i<n:
    j=0
    while j<n:
        if (list[i]+list[j]==sum):
            print(list[i],",",list[j])
        j+=1
    i+=1
