# x = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
  
# flatten_matrix = []
  
# for sublist in x:
#     for val in sublist:
#         flatten_matrix.append(val)
          
# print(flatten_matrix)


# o/p [1,2,3,4,5,6,7,8,9]
x=[[1,2,3],[4,5],[6,7,8,9]]
a=[]
i=0
while i<len(x):
    j=0
    while j<len(x[i]):
        a.append(x[i][j])
        j+=1
    i+=1
print(a)
