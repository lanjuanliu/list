# a="lanjuanliu"
# print(len(a))


# a= "Rishabh Verma"
# print (len(a))


# a = "navgurukul"
# if "n" in a:
#        print ("n hai")
# else:
#       print ("n nahi hai")
      

# max
# a=[1,2,3,4,5,6]
# i=0
# while i<len(a):
#     b=max(a)
#     i+=1
# print(b)

def numbers_less_than_twenty(list):
  counter = 0
  while counter < len(list):
item = list[counter]
if item > 20:
   list.remove(item)
else:
   counter += 1
  return list

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_sub_20 = numbers_less_than_twenty(num_list)

print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20)