#how to upload this game to a website and add front end features?

import math
import random

lower_bound = int(input("Enter lower bound : "))
upper_bound = int(input("Enter upper bound : "))

x = random.randint(lower_bound, upper_bound)

min_tries = round(math.log(upper_bound-lower_bound+1,2))

print("You have only", min_tries, "number of tries to guess the number!")

count = 0

while count <= min_tries :
    guess = int(input("Enter your guess babyG : "))
    
    if guess == x :
        print("your guess is correct!")
        print("Congratulations! You completed the game in ", count, "guesses!")
        break

    elif guess > x :
        print("you guessed higher! Try again")
    
    elif guess < x :
        print("you guessed lower! Try again")
    
    count+=1

if count > min_tries :
    print("You have exhausted number of tries!\n Better luck next time!")