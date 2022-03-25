a=[4,5,5,5,3,8]
s=len(a)
for i in range (s-2):
    if a[i]==a[i+1]and a[i+1]==a[i+2]:
        print(a[i])
