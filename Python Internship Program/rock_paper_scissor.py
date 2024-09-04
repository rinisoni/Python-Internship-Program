"""
ROCK-PAPAER-SCISSORS GAME
computer_choice=rock/paper/scossor
user_choice
"""

import random
options=["rock","paper","scissors"]
computer_choice=random.choice(options)
user_choice=input("Enter your guess [rock/paper/scissors]").lower()

if(user_choice !="rock" and user_choice != "paper" and user_choice != "scissors"):
    print("invalid choice")

elif(user_choice=="rock" and computer_choice=="scissors"):
    print("you win")

elif(user_choice=="paper" and computer_choice=="rock"):
    print("you win")

elif(user_choice=="scissors" and computer_choice=="paper"):
    print("you win")

elif(user_choice==computer_choice):
    print("TIE")
else:
    print(f"You lost,the computers choice was{computer_choice} ")

