print("Welcome to calculator!")
print("\nEnter 'end' to quit")
while True:
    user_name_inp=input("Please, enter your name: ")
    if user_name_inp=='end':
        print("Goodbye! Turtning off...")
        break
    elif user_name_inp.isalpha():
        while True:
            operation = input(f"\n{user_name_inp.capitalize()}, please, choose operation and enter it's sign: ")
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
            if operation != 'end':
                if operation=='+':
                    while True:
                        print(f"\n{user_name_inp.capitalize()}, you chose Addition for which you need 2 operands ")
                        digit_first = input(f"\n{user_name_inp.capitalize()}, input first digit ('end'-main menu): ")
                        if digit_first=='end':
                            break
                        else:
                            digit_second = input(f"{user_name_inp.capitalize()}, input second digit ('end'-main menu): ")
                            if digit_first.strip("-").replace('.','',1).isdigit() and digit_second.strip("-").replace('.','',1).isdigit():
                                digit_first = float(digit_first)
                                digit_second = float(digit_second)
                                print(f"Addition: {digit_first} + {digit_second} = {digit_first+digit_second} ")
                            else: print("\nWrong value! Please, input either float (e.g. 1.1) or integer (e.g. 1) value! Thank you! ")
                    continue    
                elif operation=='-':
                    print(f"{user_name_inp.capitalize()}, you chose Subtraction for which you need 2 operands ")
                    print(user_name_inp.capitalize()+", please enter left hand operand: ")
                    digit_first = (input())
                    digit_first_check = float(digit_first)
                    print(user_name_inp.capitalize()+", please enter right hand operand:")
                    digit_second = (input(f"{digit_first_check} - "))
                    digit_second_check = float(digit_second)
                    if type(digit_first_check)==float and type(digit_second_check)==float:
                        print(f"Addition: {digit_first_check} - {digit_second_check} = {digit_first_check-digit_second_check} ")
                    else: 
                        print("It doesn't look like digits I can work with! Please, input either float (1.0) or integer (1) value! Thank you! ")
                elif operation=='/':
                    print(f"{user_name_inp.capitalize()}, you chose Division for which you need 2 operands ")
                    print(user_name_inp.capitalize()+", please enter left hand operand: ")
                    digit_first = (input())
                    digit_first_check = float(digit_first)
                    print(user_name_inp.capitalize()+", please enter right hand operand:")
                    digit_second = (input(f"{digit_first_check} / "))
                    digit_second_check = float(digit_second)
                    if type(digit_first_check)==float and type(digit_second_check)==float:
                        print(f"Addition: {digit_first_check} / {digit_second_check} = {digit_first_check/digit_second_check} ")
                    else: 
                        print("It doesn't look like digits I can work with! Please, input either float (1.0) or integer (1) value! Thank you! ")
                elif operation=='*':
                    print(f"{user_name_inp.capitalize()}, you chose Multiplication for which you need 2 operands ")
                    print(user_name_inp.capitalize()+", please enter left hand operand: ")
                    digit_first = (input())
                    digit_first_check = float(digit_first)
                    print(user_name_inp.capitalize()+", please enter right hand operand:")
                    digit_second = (input(f"{digit_first_check} * "))
                    digit_second_check = float(digit_second)
                    if type(digit_first_check)==float and type(digit_second_check)==float:
                        print(f"Addition: {digit_first_check} * {digit_second_check} = {digit_first_check*digit_second_check} ")
                    else: 
                        print("It doesn't look like digits I can work with! Please, input either float (1.0) or integer (1) value! Thank you! ")
                elif operation=='//':
                    print(f"{user_name_inp.capitalize()}, you chose Floor Division for which you need 2 operands ")
                    print(user_name_inp.capitalize()+", please enter left hand operand: ")
                    digit_first = (input())
                    digit_first_check = float(digit_first)
                    print(user_name_inp.capitalize()+", please enter right hand operand:")
                    digit_second = (input(f"{digit_first_check} // "))
                    digit_second_check = float(digit_second)
                    if type(digit_first_check)==float and type(digit_second_check)==float:
                        print(f"Addition: {digit_first_check} // {digit_second_check} = {digit_first_check//digit_second_check} ")
                    else: 
                        print("It doesn't look like digits I can work with! Please, input either float (1.0) or integer (1) value! Thank you! ")
                elif operation=='%':
                    print(user_name_inp.capitalize()+", please enter right hand operand: ")
                    digit_second = float(input())
                    print(f"Modulus: {digit_first} % {digit_second} = {digit_first%digit_second} ")
                elif operation=='**':
                    print(user_name_inp.capitalize()+", please enter right hand operand: ")
                    digit_second = float(input())
                    print(f"Exponent: {digit_first} ** {digit_second} = {digit_first**digit_second} ")
                elif operation=='*s':
                    print(f"{user_name_inp.capitalize()}+ Perfect square of {digit_first} = {digit_first*digit_first}")
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