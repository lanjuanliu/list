# num=int(input("enter the number"))
# user=len(str(num))
# temp=num
# sum=0
# while temp>0:
#     digit=temp%10
#     sum+=digit**3
#     temp=temp//10
# if num==sum:
#     print("the num is an armstrong")
# else:
#     print("the num is not an armstrong num")

 
num=int(input("enter the number"))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp=temp//10
if num==sum:
    print("the num is an armstrong")
else:
    print("the number is not armstrong")


