print("************** QUIZ GAME **************")

print("Welcome to my GAME!!!")
print("Do you want ot play my game?")
playing = input("(y/n): ")

if(playing.lower() == "n"):
    quit()
    
print("Okay! Lets go!!")
correct = 0
wrong = 0

answer1 = input("What is the full form of CPU? ")
if(answer1.lower() == "central processing unit"):
    correct += 1
else:
    wrong += 1

answer2 = input("What is the full form of RAM? ")
if(answer2.lower() == "random access memory"):
    correct += 1
else:
    wrong += 1

answer3 = input("What is the full form of ROM? ")
if(answer3.lower() == "read only memory"):
    correct += 1
else:
    wrong += 1

answer4 = input("What is the full form of CLI? ")
if(answer4.lower() == "command line interface"):
    correct += 1
else:
    wrong += 1

answer5 = input("What is the full form of GUI? ")
if(answer5.lower() == "graphical user interface"):
    correct += 1
else:
    wrong += 1

print("Total Correct answers: "+str(correct))
print("Total Wrong answers: "+str(wrong))

print("Total Score: "+str(correct)+"/5")
percent = print("You got: "+str((correct / 5) * 100))

if(percent >= 40):
    print("Congrats! You passed the quiz!")
else:
    print("Nice Try! Better luck next time!")