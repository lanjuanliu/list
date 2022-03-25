a=["how many continent are there?","what is the capital of india?","what are we doing in ng"]
b=[["four","nine","seven","eight"],["chandhigarh","bhopal","chennai","delhi"],
["software engineering","couselling","tourism","agriculture"]]
solution=[3,4,1]
opt=[["four","seven"],["bhopal","delhi"],["software engineering","couselling"]]
sol=[2,2,1]
i=0
j=0
count=0
while i<len(a)and j<len(b):
    print(i+1,a[i])
    k=0
    while k<(len(b)+1):
        print(k+1,b[j][k])
        k+=1
    life=input("want 50 50 lifeline? enter yes or no")
    if life=="yes":
        if count==0:
            l=0
            while l<len(opt[i]):
                print(l+1,opt[i][l])
                l+=1
            count+=1
            ans=int(input("enter your lifeline"))
            if ans==sol[i]:
                print("congrate! your ans right")
            else:
                print("sorry! your ans is wrong")
                break
        else:
            print("your lifeline has been used")
            user=int(input("enter your ans"))
            if user==solution[i]:
                print("congratution!your ans is correct")
            else:
                print("xorry,better luck next tym")
                break
    elif life=="no":
        user=int(input("enter ur ans"))
        if user==solution[i]:
            print("congratution! your ans is right")
        else:
            print("xorry,better luck next time")
            break
    i+=1
    j+=1



