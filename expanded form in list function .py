# a=12
# b=a
# i=0
# while i<len(str(a)):
#     a=a%10
#     b=b//10
#     i+=1
# print(b*10,"+",a)


# a=42
# b=a
# i=0
# while i<len(str(a)):
#     a=a%10
#     b=b//10
#     i+=1
# print(b*10,"+",a)
    # user=int(input("enter ur ans"))
    # if user==solution[i]:


a=70304
b=a
i=0
while i<len(str(a)):
    a=a%100
    b=b//10
    a=a%10
    i+=1
print(b*100,"+",a)





