ques=["how many continent are there?","what is the capital of india?","what are we doing in ng?"]
option=[["four","nine","seven","eight"],["chandhigarh","bhopal","chennai","delhi"],["software engineering","couselling","tourism","agriculture"]]
solution=[3,4,1]
opt=[["seven","nine"],["chennai","delhi"],["software engineering","couselling"]]
slu=[1,2,1]
i=0
j=0
count=0
while i<len(ques) and  j<len(option):
    print(j+1,ques[i])
    k=0
    while k<(len(option)+1):
        print(k+1,option[j][k])
        k+=1
    life=input("do you want to use lifeline? enter yes/no:-")
    if life=="yes":
        if count==0:
            l=0
            while l<(len(opt[i])):
                print(l+1,opt[i][l])
                l+=1
            count+=1
            ans=int(input("enter the number:-"))
            if ans==slu[i]:
                print("congratulation")
            else:
                print("xory")

        else:
            print("Your lifeline has been used:")
            user=int(input("enter ur ans"))
            if user==solution[i]:
                print("Congrats, Ur answer is correct")
            else:
                print("Sorry, Ur answer is wrong")
            break
    elif life=="no":
        user=int(input("enter ur ans"))
        if user==solution[i]:
            print("Congrats, Ur answer is correct")
        else:
            print("Sorry, Ur answer is wrong")
    i=i+1
    j+=1

