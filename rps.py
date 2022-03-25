#!/usr/bin/python3
import random
import pyfiglet
import colorama 
from colorama import Fore, Back, init

init(autoreset=True)

b = pyfiglet.figlet_format("Rock Paper Scissors")
print(b)

you = 0
computer = 0
#while loop to count points
while you < 3 or computer < 3:

    i = input("Enter rock, paper or scissors=> ")

    l = ["rock", "paper", "scissors"]

    a = random.choice(l)
    #actual game# 
    if a == "rock" and i == "paper" or a == "paper" and i == "scissors" or a == "scissors" and i == "rock":
        print(Fore.BLACK+Back.BLUE+"You:",i)
        print(Fore.BLACK+Back.YELLOW+"Computer:",a)
        print()
        print(Fore.BLACK+Back.GREEN+"You won")
        you+=1
        print()
        print(Fore.BLACK+Back.BLUE+"You: ",you)
        print(Fore.BLACK+Back.YELLOW+"Computer: ",computer)
        print()

    elif a== "rock" and i == "rock" or a == "paper" and i == "paper" or a == "scissors" and i == "scissors":
        print(Fore.BLACK+Back.BLUE+"You:",i)
        print(Fore.BLACK+Back.YELLOW+"Computer:",a)
        print()
        print(Fore.BLACK+Back.WHITE+"Draw")
        print()
        print(Fore.BLACK+Back.BLUE+"You: ",you)
        print(Fore.BLACK+Back.YELLOW+"Computer: ",computer)
        print()
    else:
        print(Fore.BLACK+Back.BLUE+"You:",i)
        print(Fore.BLACK+Back.YELLOW+"Computer:",a)
        print()
        print(Fore.BLACK+Back.RED+"You lost")
        computer+=1
        print()
        print(Fore.BLACK+Back.BLUE+"You: ",you)
        print(Fore.BLACK+Back.YELLOW+"Computer: ",computer)
        print()
   ################## 

    if computer == 3:
        print(Fore.BLACK+Back.MAGENTA+"Computer Won")
        break
    elif you == 3:
        print(Fore.BLACK+Back.MAGENTA+"You Won")
        break
