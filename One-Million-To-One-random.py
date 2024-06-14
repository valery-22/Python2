print("Totally Random One-Million-To-One")
print()
import random 
counter = 1
correct_number = random.randint(1,1000000)
guess = 0
while True:
    guess = int(input("What is your guess?:"))
    if guess < correct_number:
        print("Too low, try again!")
        counter += 1
    elif(guess > correct_number):
        print("Too high, try again!")
        counter += 1
    elif(guess == correct_number):
        print("Correct!")
        print("It took you", counter, "Guesses to get the number correct.")
    else:
        print("That is not a number I recognize.")
    break 
