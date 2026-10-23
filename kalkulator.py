print(r"""
           _            _       _             
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
""")

try:
    while True: 

        while True: 
            print ("enter a")
            try:
                a = float(input())
                break
            except ValueError:
                print("this is not number")

        while True:
            print("choose an operator(+, -, *, /, **, root)")
            operator = input()
            if operator in ("+", "-", "*", "/","**","root"):
                break
            else:
                print("this is not an operator")

        while True: 
            print ("enter b")
            try:
                b = float(input())
            except ValueError:
                print("this is not number")
                continue
            
            if operator == "/" and b == 0:
                print("dont divide by 0")
                continue

            if operator =="**":
                if a == 0 and b < 0:
                    print("0 cant be raised to a negative power")
                    continue
                if a < 0 and not b.is_integer():
                    print("negative number cant be raised to a fractional power")
                    continue

            if operator == "root":
                if b == 0:
                    print*("root deegree cant be 0")
                    continue
                if a < 0:
                    print("cant take root out of negative number")
            break

        if operator == "+":
            result = a + b 

        elif operator == "-":
            result = a - b 
            
        elif operator == "*":
            result = a * b 
            
        elif operator == "/":
            result = a / b 

        elif operator == "**":
            result = a ** b 

        elif operator == "root":
            result = a ** (1 / b)

        result = round(result, 10)
        
        if result.is_integer():
            result = int(result)

        print("=", result)
        

except (KeyboardInterrupt, EOFError):
    try:
        print("\ngoodbye")
    except KeyboardInterrupt:
        pass






