elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even_count=0
odd_count=0
sum_even=0
sum_odd=0
avg_even=0
avg_odd=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        even_count+=1
        sum_even=sum_even+elements[i]
        avg_even=sum_even//even_count
    else:
        odd_count+=1
        sum_odd=sum_odd+elements[i]
        avg_odd=sum_odd//odd_count
    i+=1
print("count of even",even_count)
print("count of odd",odd_count)
print("sum of even",sum_even)
print("sum of odd",sum_odd)
print("avg of even",avg_even)
print("avg of odd",avg_odd)