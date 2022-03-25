ele=[23,14,56,12,19,9,15,25,31,42,43]
even_sum=0
odd_sum=0
i=0
while i<len(ele):
    if ele[i]%2==0:
        even_sum=ele[i]+even_sum
    else:
        odd_sum=ele[i]+odd_sum
    i+=1
print("even_sum",even_sum)
print("odd_sum",odd_sum)