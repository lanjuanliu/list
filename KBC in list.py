ques=["how many continent are there?","what is the capital of india?","what are we doing in ng?"]
option=[["four","nine","seven","eight"],["chandhigarh","bhopal","chennai","delhi"],["software engineering","couselling","tourism","agriculture"]]
solution=[3,4,1]
i=0
while i<len(ques):
    print(i+1,ques[i])
    i=i+1
i=0
while i<len(ques):
    print("Q",i+1,ques[i])
    j=0
    while j<(len(option)+1):
        print(j+1,option[i][j])
        j+=1   
    user=int(input("enter ur ans"))
    if user==solution[i]:
        print("true")
    else:
        print("false")
    i=i+1





            









