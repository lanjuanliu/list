end=("ABBBBCCCCCAB")
i=0
while i<=(len(end)-1):
    count=1
    ch=end[i]
    j=1
    while (j<len(end)-1):
        if end[j]==end[j+1]:
            count=count+1
            j=j+1
        else:
            break
    end=end+str(count+ch)
    i=j+1
print(end)