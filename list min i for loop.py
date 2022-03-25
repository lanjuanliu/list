list=[21,3,6,9,54,1,8,10]
min=list[0]
for i in range (len(list)):
    if list[i]<min:
        min=list[i]
print("the smallest element is:",min)