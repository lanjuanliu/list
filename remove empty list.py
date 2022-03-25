lst=[(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]
i=0
b=[]
while i<len(lst):
    if  lst[i] == ():
        del(lst[i])
    i+=1
print(lst)
