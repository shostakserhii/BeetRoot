print("\nWelcome to calculator!")
print("\nEnter 'end' to quit")
while True:
    user_name_inp=input("Please, enter your name ('end' to exit): ")
    if user_name_inp=='end':
        print("Goodbye! Turtning off...")
        break
    elif user_name_inp.isalpha():
        while True:
            print(" Enter '+' for Addition ")
            print(" Enter '-' for Subtraction ")
            print(" Enter '/' for Division ")
            print(" Enter '*' for Multiplication ")
            print(" Enter '//' for Floor Division ")
            print(" Enter '%' for Modulus ")
            print(" Enter '**' Exponent ")
            print(" Enter '*s' for Perfect Square ")
            print(" Enter 'r' for Rounding ")
            print(" Enter 'end' to close application ")
            print(" Enter 'rnd' for Randomizer ")
            print(" Enter 'auto' to enter automode ")
            operation = input(f"\n{user_name_inp.capitalize()}, please, choose operation and enter it's sign: ")
            if operation != 'end':
                if operation=='+':
                    while True:
                        print(f"\n{user_name_inp.capitalize()}, you chose Addition for which you need 2 operands ")
                        digit_first = input(f"\n{user_name_inp.capitalize()}, input first digit ('end'-main menu): ")
                        if digit_first=='end':
                            break
                        else:
                            digit_second = input(f"{user_name_inp.capitalize()}, input second digit ('end'-main menu): ")
                            if digit_first.lstrip("-").replace('.','',1).isdigit() and digit_second.lstrip("-").replace('.','',1).isdigit() and digit_first.count("-")<=1 and digit_second.count("-")<=1:
                                digit_first = float(digit_first)
                                digit_second = float(digit_second)
                                print(f"Addition: {digit_first} + {digit_second} = {digit_first+digit_second} ")
                            else: print("\nWrong value! Please, input either float (e.g. 1.1) or integer (e.g. 1) value! Thank you! ")
                    continue
                elif operation=='-':
                    while True:
                        print(f"\n{user_name_inp.capitalize()}, you chose Subtraction for which you need 2 operands ")
                        digit_first = input(f"\n{user_name_inp.capitalize()}, input first digit ('end'-main menu): ")
                        if digit_first=='end':
                            break
                        else:
                            digit_second = input(f"{user_name_inp.capitalize()}, input second digit ('end'-main menu): ")
                            if digit_first.lstrip("-").replace('.','',1).isdigit() and digit_second.lstrip("-").replace('.','',1).isdigit() and digit_first.count("-")<=1 and digit_second.count("-")<=1:
                                digit_first = float(digit_first)
                                digit_second = float(digit_second)
                                print(f"Subtraction: {digit_first} - {digit_second} = {digit_first-digit_second} ")
                            else: print("\nWrong value! Please, input either float (e.g. 1.1) or integer (e.g. 1) value! Thank you! ")
                    continue
                elif operation=='/':
                    while True:
                        print(f"\n{user_name_inp.capitalize()}, you chose Division for which you need 2 operands ")
                        digit_first = input(f"\n{user_name_inp.capitalize()}, input first digit ('end'-main menu): ")
                        if digit_first=='end':
                            break
                        else:
                            digit_second = input(f"{user_name_inp.capitalize()}, input second digit ('end'-main menu): ")
                            if digit_second==0:
                                print("\n\tError: you cannot devide by 0, try something else ")
                            elif digit_first.lstrip("-").replace('.','',1).isdigit() and digit_second.lstrip("-").replace('.','',1).isdigit() and digit_first.count("-")<=1 and digit_second.count("-")<=1:
                                digit_first = float(digit_first)
                                digit_second = float(digit_second)
                                print(f"Division: {digit_first} / {digit_second} = {digit_first/digit_second} ")
                            else: print("\nWrong value! Please, input either float (e.g. 1.1) or integer (e.g. 1) value! Thank you! ")
                    continue
                elif operation=='*':
                    while True:
                        print(f"\n{user_name_inp.capitalize()}, you chose Multiplication for which you need 2 operands ")
                        digit_first = input(f"\n{user_name_inp.capitalize()}, input first digit ('end'-main menu): ")
                        if digit_first=='end':
                            break
                        else:
                            digit_second = input(f"{user_name_inp.capitalize()}, input second digit ('end'-main menu): ")
                            if digit_first.lstrip("-").replace('.','',1).isdigit() and digit_second.lstrip("-").replace('.','',1).isdigit() and digit_first.count("-")<=1 and digit_second.count("-")<=1:
                                digit_first = float(digit_first)
                                digit_second = float(digit_second)
                                print(f"Multiplication: {digit_first} * {digit_second} = {digit_first*digit_second} ")
                            else: print("\nWrong value! Please, input either float (e.g. 1.1) or integer (e.g. 1) value! Thank you! ")
                    continue
                elif operation=='//':
                    while True:
                        print(f"\n{user_name_inp.capitalize()}, you chose Floor Division for which you need 2 operands ")
                        digit_first = input(f"\n{user_name_inp.capitalize()}, input first digit ('end'-main menu): ")
                        if digit_first=='end':
                            break
                        else:
                            digit_second = input(f"{user_name_inp.capitalize()}, input second digit ('end'-main menu): ")
                            if digit_second==0:
                                print("\n\tError: you cannot devide by 0, try something else ")
                            elif digit_first.lstrip("-").replace('.','',1).isdigit() and digit_second.lstrip("-").replace('.','',1).isdigit() and digit_first.count("-")<=1 and digit_second.count("-")<=1:
                                digit_first = float(digit_first)
                                digit_second = float(digit_second)
                                print(f"Floor Division: {digit_first} // {digit_second} = {digit_first//digit_second} ")
                            else: print("\nWrong value! Please, input either float (e.g. 1.1) or integer (e.g. 1) value! Thank you! ")
                    continue
                elif operation=='%':
                    while True:
                        print(f"\n{user_name_inp.capitalize()}, you chose Modulus for which you need 2 operands ")
                        digit_first = input(f"\n{user_name_inp.capitalize()}, input first digit ('end'-main menu): ")
                        if digit_first=='end':
                            break
                        else:
                            digit_second = input(f"{user_name_inp.capitalize()}, input second digit ('end'-main menu): ")
                            if digit_second==0:
                                print("\n\tError: you cannot devide by 0, try something else ")
                            elif digit_first.lstrip("-").replace('.','',1).isdigit() and digit_second.lstrip("-").replace('.','',1).isdigit() and digit_first.count("-")<=1 and digit_second.count("-")<=1:
                                digit_first = float(digit_first)
                                digit_second = float(digit_second)
                                print(f"Modulus: {digit_first} % {digit_second} = {digit_first%digit_second} ")
                            else: print("\nWrong value! Please, input either float (e.g. 1.1) or integer (e.g. 1) value! Thank you! ")
                    continue
                elif operation=='**':
                    while True:
                        print(f"\n{user_name_inp.capitalize()}, you chose Exponent for which you need 2 operands ")
                        digit_first = input(f"\n{user_name_inp.capitalize()}, input first digit/body ('end'-main menu): ")
                        if digit_first=='end':
                            break
                        else:
                            digit_second = input(f"{user_name_inp.capitalize()}, input second digit/power ('end'-main menu): ")
                            if digit_first.lstrip("-").replace('.','',1).isdigit() and digit_second.lstrip("-").replace('.','',1).isdigit() and digit_first.count("-")<=1 and digit_second.count("-")<=1:
                                digit_first = float(digit_first)
                                digit_second = float(digit_second)
                                print(f"Exponent: {digit_first} ** {digit_second} = {digit_first**digit_second} ")
                            else: print("\nWrong value! Please, input either float (e.g. 1.1) or integer (e.g. 1) value! Thank you! ")
                    continue
                elif operation=='*s':
                    while True:
                        print(f"\n{user_name_inp.capitalize()}, you chose Perfect Square ")
                        digit_first = input(f"\n{user_name_inp.capitalize()}, input digit ('end'-main menu): ")
                        if digit_first=='end':
                            break
                        else:
                            if digit_first.strip("-").replace('.','',1).isdigit():
                                digit_first = float(digit_first)
                                print(f"Perfect Square of {digit_first} = {digit_first*digit_first} ")
                            else: print("\nWrong value! Please, input either float (e.g. 1.1) or integer (e.g. 1) value! Thank you! ")
                    continue
                if operation=='rnd':
                    while True:
                        print(f"\n{user_name_inp.capitalize()}, you chose Randomizer ")
                        digit_first = input(f"\n{user_name_inp.capitalize()}, set the range from ('end'-main menu): ")
                        if digit_first=='end':
                            break
                        else:
                            digit_second = input(f"{user_name_inp.capitalize()}, input the end of the range ('end'-main menu): ")
                            if digit_first.lstrip("-").replace('.','',1).isdigit() and digit_second.lstrip("-").replace('.','',1).isdigit() and digit_first.count("-")<=1 and digit_second.count("-")<=1:
                                digit_first = float(digit_first)
                                digit_second = float(digit_second)
                                import random
                                #print(f"Random number of range from {digit_first} to {digit_second} is: {random(digit_first,digit_second)}")
                                print("The random is ", random.randrange(digit_first,digit_second))
                            else: print("\nWrong value! Please, input either float (e.g. 1.1) or integer (e.g. 1) value! Thank you! ")
                    continue
                print(" Enter '+' for Addition ")
                print(" Enter '-' for Subtraction ")
                print(" Enter '/' for Division ")
                print(" Enter '*' for Multiplication ")
                print(" Enter '//' for Floor Division ")
                print(" Enter '%' for Modulus ")
                print(" Enter '**' Exponent ")
                print(" Enter '*s' for Perfect Square ")
                print(" Enter 'r' for Rounding")
                print(" Enter 'end' to close application")
                continue
            print(f"{user_name_inp.capitalize()}, thanks for using our calculator!")
            break
    else: print("It is not name")
    continue