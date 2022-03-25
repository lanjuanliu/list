# a=[1,2,7,9,10]
# print(a[::3])


# a=[2,3,7,12,15,17,6]
# print(a[5])


# x=[[1,2],[2,7,9],[5,6,11]]
# print(x[0][0],x[1][1],x[2][2])


# a=[2,7,9,11]
# a.insert(1,6)
# print(a)


# a=[2,3,7,9,12,11,14,17,10]
# b=[]
# c=[]
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i+=1
# print(b)
# print(c)


a=[[56,9],[34,3],[3,78],[98,100]]
i=0
c=[]
while i<len(a):
    j=0
    b=[]
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j+=1
    b.append(sum)
    c.append(b)
    i+=1
print(c)  


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("Recursion Example Results")
tri_recursion(6)
