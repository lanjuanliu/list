from tkinter import N


char = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
while i<len(char):
    a=char.count("a")
    b=char.count("n")
    c=char.count("t")
    d=char.count("x")
    e=char.count("u")
    f=char.count("g")
    i+=1
print("count a",a)
print("count n",b)
print("count t",c)
print("count x",d)
print("count u",e)
print("count g",f)



