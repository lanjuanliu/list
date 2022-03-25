# a=["a",1,"2",5,"b","q"]
# user=int(input("enter the number"))
# i=-user
# while i<=-1:
#     print(a[i])
#     i+=1


a=["a",1,"2",5,"b","q"]
user=int(input("enter the number"))
i=1
while i<=user-3:
    print(a[-i])
    i+=1
    