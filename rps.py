#!/usr/bin/python3
import random
import pyfiglet

b = pyfiglet.figlet_format("Rock Paper Scissors")
print(b)

i = input("Enter rock, paper or scissors=> ")

l = ["rock", "paper", "scissors"]

a = random.choice(l)

if a == "rock" and i == "paper" or a == "paper" and i == "scissors" or a == "scissors" and i == "rock":
    print("You:",i)
    print("Computer:",a)
    print("You won")
elif a== "rock" and i == "rock" or a == "paper" and i == "paper" or a == "scissors" and i == "scissors":
    print("You:",i)
    print("Computer:",a)
    print("Draw")
else:
    print("You:",i)
    print("Computer:",a)
    print("You lost")