from random import randint, choice
from tkinter import *

root = Tk()

root.geometry("600x500")
root.title("Python Micro Project")

questionLabel = None
resultLabel = None


#root.configure(bg="black")
root.resizable(0, 0)

question = StringVar()
answer = StringVar()
givenAnswer = StringVar()
score = IntVar()
questionNumber = IntVar()

def generateQuestions():

    global questionLabel

    questionNumber.set(questionNumber.get() + 1)

    answer.set(0)
    num1 = randint(1, 10)
    num2 = randint(1, 10)

    operator = choice(['+', '-', '*'])
    
    question.set(str(num1) + operator + str(num2))
    answer.set(eval(question.get()))

    if questionLabel:
        questionLabel.destroy()
    
    questionLabel = Label(root, text=f"Question: {question.get()}", font=('arial', 15))
    questionLabel.grid(row=2, column=0)

def checkAnswer():

    global resultLabel
    global scoreLabel

    if questionNumber.get() > 10:
        return


    if resultLabel:
        resultLabel.destroy()

    if str(answer.get()) == givenAnswer.get():
        score.set(score.get() + 1)
        resultLabel = Label(root, text="Correct", font=('arial', 15), fg="green")
        resultLabel.grid(row=5, column=0)

        scoreLabel = Label(root, text=f"Score: {score.get()}", font=('arial', 15), fg="black")
        scoreLabel.grid(row=6, column=0)

    else:
        resultLabel = Label(root, text="Incorrect", font=('arial', 15), fg="red")
        resultLabel.grid(row=5, column=0)

    if questionNumber.get() == 10:
        scoreLabel.destroy()
        scoreLabel = Label(root, text=f"Final Score: {score.get()}", font=('arial', 15), fg="black")
        scoreLabel.grid(row=6, column=0)
    else:
        generateQuestions()

def restart():

    global scoreLabel
    scoreLabel.destroy()
    score.set(0)
    questionNumber.set(0)
    generateQuestions() 

    scoreLabel = Label(root, text=f"Score: {score.get()}", font=('arial', 15), fg="black")
    scoreLabel.grid(row=6, column=0)


#****************User Interface****************
headingLabel = Label(root, text = "Quiz Game", font=('arial', 20))
headingLabel.grid(row=0, column=0)

questionScale = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=400, variable=questionNumber)
questionScale.grid(row=1, column=0)

completeQuestionLabel = Label(root, text="10th Question", font=('arial', 15))
completeQuestionLabel.grid(row=1, column=1)

questionLabel = Label(root, text=question.get(), font=('arial', 15))
questionLabel.grid(row=2, column=0)

#Entry
answerEntry = Entry(root, textvariable=givenAnswer ,font=('arial', 15))
answerEntry.grid(row=3, column=0)

#Button
submitButton = Button(root, text="Submit", font=('arial', 15), command= checkAnswer)
submitButton.grid(row=4, column=0)

resultLabel = Label(root, text="Results", font=('arial', 15), fg="blue")
resultLabel.grid(row=5, column=0)

scoreLabel = Label(root, text=f"Score: {score.get()}", font=('arial', 15), fg="black")
scoreLabel.grid(row=6, column=0)

restartButton = Button(root, text="Restart", font=('arial', 15), command= restart)
restartButton.grid(row=7, column=0)

generateQuestions() 

root.mainloop()
