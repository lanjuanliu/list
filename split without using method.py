n="my name is teresa"
b=[]
a=""
# for c in n:
#     if c==" ":
#         b.append(a)
#         a=" "
#     else:
#         a=a+c
# if a:
#     b.append(a)
# print(b)


x="My name is Lan"
a=' '
b=[]
i=0
while  i<len(x):
    if x[i]==" ":
        b.append(a)
        a=" "
    else:
        a+=x[i]
    i+=1
if a:
    b.append(a)
print(b)


