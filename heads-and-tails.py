#!bin/python3
import random
import colorama
from colorama import Fore, Back, init

init(autoreset=True)

i =random.randrange(1, 3)

if i == 1:
    print(Fore.BLACK+Back.BLUE+"Heads")
elif i == 2:
    print(Fore.BLACK+Back.RED+"Tails") 
