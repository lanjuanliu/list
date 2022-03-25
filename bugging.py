marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
total = 0
counter = 0
i=0
while counter < len(marks):
    total=total+int(marks[counter])
    counter=counter+1
    i=i+1
print("it is total",total)
print("it is counter",counter)
