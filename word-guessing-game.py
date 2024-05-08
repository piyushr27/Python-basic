import math
import random

list = ["cat", "dog", "car", "bat", "elf", "sit", "gut", "god", "pay"]

key = random.choice(list)

name = input("Enter your name : ")
print("Good luck ", name, "!")

count = 0

guesses = ""

while (count <= 12) :
    count += 1
    guess = input("\nGuess an alphabet : ")

    if (guess in key) & (guess not in guesses):
        guesses += guess
        for char in key :
            if (char in guesses) :
                print(char, end = ' ')
            else :
                print('_', end = ' ')

    if (sorted(key) == sorted(guesses)) :
        print("\nCongratulations! You've guessed the word", key)
        break
    
    elif (guess not in key) :
        for char in key :
            if (char in guesses) :
                print(char, end = ' ')
            else :
                print('_', end = ' ')
        print("\nIncorrect guess! Try again :")

if count > 12 :
    print("You have exhausted number of tries!\n Better luck next time!")