from random import randint, choice
from tkinter import *

root = Tk()
root.geometry("700x600")
root.title("Python Micro Project")

# Configure background color
root.configure(bg="#e6e6e6")

questionLabel = None
resultLabel = None

# Configure font styles
heading_font = ('arial', 30, 'bold')
label_font = ('arial', 18)
button_font = ('arial', 15, 'bold')

# Global variables
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
    
    if operator == '*':
        # Ensure multiplication is displayed with 'x' instead of '*'
        display_operator = 'x'
    else:
        display_operator = operator

    question_text = f"Question {questionNumber.get()}: {num1} {display_operator} {num2}"
    question.set(question_text)

    # Calculate the answer without using eval()
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2

    answer.set(correct_answer)

    if questionLabel:
        questionLabel.config(text=question_text)
    else:
        questionLabel = Label(root, text=question_text, font=label_font, bg="#e6e6e6")
        questionLabel.grid(row=2, column=0, pady=20, sticky='nsew')


def checkAnswer():
    global resultLabel
    global scoreLabel

    if questionNumber.get() > 10:
        return

    if resultLabel:
        resultLabel.destroy()

    if str(answer.get()) == givenAnswer.get():
        score.set(score.get() + 1)
        resultLabel = Label(root, text="Correct!", font=label_font, fg="green", bg="#e6e6e6")
        resultLabel.grid(row=5, column=0, pady=10, sticky='nsew')

        scoreLabel.config(text=f"Score: {score.get()}", fg="black")
    else:
        resultLabel = Label(root, text="Incorrect. Try again!", font=label_font, fg="red", bg="#e6e6e6")
        resultLabel.grid(row=5, column=0, pady=10, sticky='nsew')

    if questionNumber.get() == 10:
        scoreLabel.config(text=f"Final Score: {score.get()}")
    else:
        generateQuestions()

def restart():
    global scoreLabel
    scoreLabel.destroy()
    score.set(0)
    questionNumber.set(0)
    generateQuestions() 

    scoreLabel = Label(root, text=f"Score: {score.get()}", font=label_font, fg="black", bg="#e6e6e6")
    scoreLabel.grid(row=6, column=0, pady=10, sticky='nsew')

# User Interface
headingLabel = Label(root, text="Quiz Game", font=heading_font, bg="#e6e6e6", fg="#333333")
headingLabel.grid(row=0, column=0, pady=20, sticky='nsew')

questionScale = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=400, variable=questionNumber, label="Question Number", bg="#e6e6e6", fg="#333333", font=label_font)
questionScale.grid(row=1, column=0, pady=10, sticky='nsew')


questionLabel = Label(root, text=question.get(), font=label_font, bg="#e6e6e6", fg="#333333")
questionLabel.grid(row=2, column=0, pady=20, sticky='nsew')

# Entry
answerEntry = Entry(root, textvariable=givenAnswer, font=label_font, bg="#ffffff")
answerEntry.grid(row=3, column=0, pady=10)

# Button
submitButton = Button(root, text="Submit", font=button_font, command=checkAnswer, bg="#4caf50", fg="#ffffff")
submitButton.grid(row=4, column=0, pady=20, )

resultLabel = Label(root, text="Results", font=(label_font[0], label_font[1], 'underline'), fg="#2196f3", bg="#e6e6e6")
resultLabel.grid(row=5, column=0, pady=10, sticky='nsew')

scoreLabel = Label(root, text=f"Score: {score.get()}", font=label_font, fg="black", bg="#e6e6e6")
scoreLabel.grid(row=6, column=0, pady=20, sticky='nsew')

restartButton = Button(root, text="Restart", font=button_font, command=restart, bg="#ff9800", fg="#ffffff")
restartButton.grid(row=7, column=0, pady=20, )

# Set column and row weights to make everything centered
for i in range(8):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(0, weight=1)

generateQuestions() 

root.mainloop()
