a=[10, -21, 4, -45, 66, -93, 1]
count_pos=0
count_neg=0
i=0
while i<len(a):
    if a[i]>=0:
        count_pos+=1
    else:
        count_neg+=1
    i+=1
print("count of positive",count_pos)
print("count of negative",count_neg)
  