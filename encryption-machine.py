#!bin/python3
import time
from database import pass_data
import hashlib

def encryption_machine():
  import pyfiglet

  banner = pyfiglet.figlet_format("Encryption Machine")
  print(banner)

    #just a variable
  alph = "abcdefghijklmnopqrstuvwxyz"

      #message
  f = input("Enter to encode word=> ")

  rot13 = lambda x: "".join([alph[(alph.find(c) + 13) %len(f)] for c in x])
      
  i = rot13(f)

  a = pyfiglet.figlet_format(i, font='hex')

  print("Encoded text=> ", a)

  print("Number of letters moved in rot13:",len(f))


#password authentication
i = input("Please enter password to continue=> ")

h = hashlib.md5(i.encode())
ha = h.hexdigest()

#the .sleep is just there to make it look like the programm is actually doing something that take a second instead of just 
#checking if two values are the same

#initialization loop 
if pass_data() in str(ha):
  time.sleep(1)
  print(encryption_machine())
else:
  time.sleep(1)
  print("Wrong password")
  time.sleep(1)
  print("Cancelling Process...")
  time.sleep(1)