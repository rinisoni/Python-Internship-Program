"""
SIMPLE GUESSING GAME
secret_number= Generate a random number (1-10)

user_number=Ask from user

You WON
You LOST, the number was secret_number
"""
import random

secret_number=random.randint(1,10)
user_number=int(input("Enter your guessed number"))
if(user_number==secret_number):
    print("You WON")
else:
    print("You LOST, the number is:",secret_number)