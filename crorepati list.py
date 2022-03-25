num = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
crore=0
lakh=0
dilwale=0
i=0
while i<len(num):
    if num[i]>10000000:
        crore+=1
    elif num[i]>1000000:
        lakh+=1
    elif num[i]>100000:
        dilwale+=1
    i+=1
print(crore,"crore pati")
print(lakh,"lakh pati")
print(dilwale,"dilwale")
        

