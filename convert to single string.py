# a=['a',1,'2',5,'b','q']
# b=input("enter the number")
# a.reverse()
# print(a)
# i=0
# while i<len(a):
#     i+=1
# print(a[i])
        


list1=[['a','b','c'],['d','e'],['f','g']]
i=0
b=[]
while i<len(list1):
    if type (list1[i])==type([]):
        j=0
        while j<len(list1[i]):
            b.append(list1[i][j])
            j=j+1
    else:
        b.append(list1[i])
        
    i+=1
print(b)    