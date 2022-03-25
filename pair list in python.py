a=[[4, 5, 6], [2, 4, 5], [6, 7, 5]]
b=[]
for i in a:
    b.append([[ele,i[-1]]for ele in i[:-1]])
print(b)





