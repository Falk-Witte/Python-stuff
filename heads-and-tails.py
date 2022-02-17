#!bin/python3
def heads_tails():
    import random

    i =random.randrange(1, 3)

    if i == 1:
        print("Heads")
    elif i == 2:
        print("Tails")
    
    return