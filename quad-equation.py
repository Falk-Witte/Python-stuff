#!/usr/bin/python3
from http.cookiejar import FileCookieJar
import math 
from math import sqrt
import pyfiglet

i = pyfiglet.figlet_format("Quad-Equation")
print(i)

a = int(input("Enter for a=> "))
b = int(input("Enter for b=> "))
c = int(input("Enter for c=> "))

x1 = (-b+sqrt(pow(b, 2)-4*a*c))/2*a
x2 = (-b-sqrt(pow(b, 2)-4*a*c))/2*a

print(x1)
print(x2)



