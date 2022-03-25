#!/usr/bin/python3
import math 
from math import sqrt
import pyfiglet
import colorama
from colorama import init, Fore, Back

init(autoreset=True)

i = pyfiglet.figlet_format("Quad-Equation")
print(i)

a = int(input("Enter for a=> "))
b = int(input("Enter for b=> "))
c = int(input("Enter for c=> "))

x1 = (-b+sqrt(pow(b, 2)-4*a*c))/2*a
x2 = (-b-sqrt(pow(b, 2)-4*a*c))/2*a

strx1 = str(x1)
strx2 = str(x2)
print(Fore.BLACK+Back.BLUE+strx1)
print(Fore.BLACK+Back.RED+strx2)



