a=[2, -7, 5, -64, -14]
count_pos=0
count_neg=0
i=0
while i<len(a):
    if a[i]<0:
        count_neg+=1
    else:
        count_pos+=1
    i+=1
print(count_neg)
print(count_pos)