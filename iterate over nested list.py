a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]  
i=0
a1=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        a1.append(a[i][j])
        k=1
        while k<len(a1):
            k+=1
        print(k,end=" ")
        j+=1
    i+=1

# i=0
# a1=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         a1.append(a[i][j])
#         # k=1
#         # while k<len(a1):
#         #     k+=1
#         print(a1,end=" ")
#         j+=1
#     i+=1


