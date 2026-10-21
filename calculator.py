print(r"""
           _            _       _             
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
""")
try:
    while True:
        digitsandnumbers = []

        while True:
            while True:
                number = input("Type a number:")
                if number.isdigit():
                    break
                print("This is not a number")
            digitsandnumbers.append(number)
            while True:     
                operator = input("Type an operator:")
                if operator in ("+", "-","*","/","="):
                    break
                print("This is not an operator")
            if operator == "=" :
                break
            digitsandnumbers.append(operator)

        equation = " ".join(digitsandnumbers)
        try:
            print(equation, "=", eval(equation))
        except ZeroDivisionError:
                print("dont divide by 0")
except (KeyboardInterrupt, EOFError):
    print("\ngoodbye")










