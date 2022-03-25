# a=[1,[7,9,3],[3,[9,[[2,4]]],4],5]
# print(a[1][0])
# print(a[1][1])
# print(a[2][1][0])
# print(a[2][2])
# print(a[3])


binary= [1, 0, 0, 1, 1, 0, 1, 1]
total=0
a=len(binary)
for i in range(a):
    last_element=binary
    if last_element=="1":
        total+=pow(2,i)
print("the decimal no is", total)