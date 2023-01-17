
import random

name = input("Enter your name: ")
score=0

def question(question,answer):
    global name
    global score
    count = 0
    while count < 3:
        print(question,"\n \n")
        userInput = (input("Enter the answer: ")).lower()
        if userInput == answer:
            score+=1
            print(name," Correct \nScore: ",score)
            break
        else:
            print(name," Incorrect \nScore: ", score)
            count+=1

x=True
while x == True:
    p1 = random.randint(1,1000)
    p2 = random.randint(1,1000)
    questionFuncInput = ("what is "+str(p1)+"*"+str(p2))
    answerInput = str(p1*p2)
    question(questionFuncInput,answerInput)