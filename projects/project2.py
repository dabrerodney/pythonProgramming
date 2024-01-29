print("********** NUMBER GUESSING GAME **********")
import random

r = random.randrange(1, 11)
#   randrange is used to generate random numbers between the start till end-1
#   randint is used to generate random numbers between start till end

number = int(input("Enter the number"))

if r == number:
    print("Correct guess!!")
else:
    print("Wrong guess!!")
    print("Correct number: ",r)