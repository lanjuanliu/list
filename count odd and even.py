elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 4]
even_count=0
odd_count=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        even_count+=1
    else:
        odd_count+=1
    i+=1
print("number of even element",even_count)
print("number of odd element",odd_count)
