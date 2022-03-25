elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
sum=0
sum1=0
odd=0
even=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        even+=1
        sum+=elements[i]
        average_even=sum//even
    else:
        odd+=1
        sum1+=elements[i]
        average_odd=sum1//odd
    i+=1
print("average of even",average_even)
print("average of odd",average_odd)
