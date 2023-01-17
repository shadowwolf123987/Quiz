
import random

score=0

name = input("Enter your name: ")

def question(question,answer):
    global name
    global score
    count = 0 #Attempts number

    while count < 3:

        print(question,"\n \n")

        if name.lower() == "cheatmode": #Secret hack
            userInput = answer

        else:
            userInput = (input("Enter the answer: ")).lower() #Checks if input matches answer

        if userInput == answer: #Executes if correct
            score+=1
            print(name," Correct \nScore: ",score)
            break

        else: #Executes if incorrect
            print(name," Incorrect \nScore: ", score)
            count+=1

x=True
while x == True:
    
    choice = random.randint(1,4) #Random number to decide whether to multiply or divide...
    
    p1 = random.randint(1,1000) # Random numbers to multiply together
    p2 = random.randint(1,1000)
    
    if choice == 1:
        questionFuncInput = ("what is "+str(p1)+"*"+str(p2))
        answerInput = str(p1*p2)

    if choice == 2:
        questionFuncInput = ("what is "+str(p1)+"/"+str(p2))
        answerInput = str(p1/p2)

    if choice == 3:
        questionFuncInput = ("what is "+str(p1)+"+"+str(p2))
        answerInput = str(p1+p2)

    if choice == 4:
        questionFuncInput = ("what is "+str(p1)+"-"+str(p2))
        answerInput = str(p1-p2)

    question(questionFuncInput,answerInput) #Calls function with question and answer