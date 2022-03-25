n=int(input("Enter the number:"))
list=[]
even_count=0
odd_count=0
i=0
while i<n:
    num=int(input("enter the number:"))
    list.append(num)
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
    i+=1
print(list)
print("count of even is",even_count )
print("count of odd",odd_count)


