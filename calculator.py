def my_calculator():
    import pyfiglet

    i = pyfiglet.figlet_format("Calculator")
    print(i)

    num1 = float(input("Enter for first number=> "))
    num2 = float(input("Enter for second number=> "))
    type = input("""
    a(add)
    s(subtract)
    d(divide)
    m(multiply)
    => """)

    if type == 'a':
        print(num1+num2)
    elif type == 's':
        print(num1-num2)
    elif type == 'd':
        print(num1/num2)
    else:
        print(num1*num2)

    return

print(my_calculator())    



