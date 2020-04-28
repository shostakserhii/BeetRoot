import random
operations = ('+','-','/','*','//','%','**','*s','r','rnd','end')
print("""

                       WELCOME TO CALCUTATOR!  


""")
while True:
    user_name_inp=input("Please, enter your name ('end' to exit): ")
    if user_name_inp=='end':
        print("Goodbye! Turtning off...")
        break
    elif user_name_inp.isalpha():
        while True:
            print(""" 
 __________________________         
|   OPERATION   |  Symbol  |
|Addition       |    +     |
|Division       |    /     | 
|Multiplication |    *     |
|Floor Division |    //    |
|Modulus        |    %     |
|Exponent       |    **    |
|Perfect Square |    *s    |
|Rounding       |    r     |
|Randomizer     |    rnd   |
**************************** 
'auto' to enter automode
'end' to close application ")
 """)
            operation = input(f"\n{user_name_inp.capitalize()}, please, choose operation by entering it's sign: ")
            if operation == 'end':
                break
            elif operation=='+':
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
                        break
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
            elif operation=='rnd':
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
                            #print(f"Random number of range from {digit_first} to {digit_second} is: {random(digit_first,digit_second)}")
                            if digit_first < digit_second:
                                print(f"Random num between {digit_first} and {digit_second} is {random.randrange(digit_first,digit_second)}")
                            elif digit_first==digit_second:
                                print("Numbers are equal")
                            else:
                                print(f"Random num between {digit_second} and {digit_first} is {random.randrange(digit_second,digit_first)}")
                        else: print("\nWrong value! Please, input either float (e.g. 1.1) or integer (e.g. 1) value! Thank you! ")
                continue
            elif operation=='r':
                while True:
                    print(f"\n{user_name_inp.capitalize()}, you chose Rounding ")
                    digit_first = input(f"\n{user_name_inp.capitalize()}, input digit ('end'-main menu): ")
                    if digit_first=='end':
                        break
                    else:
                        digit_second = input(f"{user_name_inp.capitalize()}, input the integer number of decimal places ('end'-main menu): ")
                        if int(digit_second) == False:
                            print("Error. Number of decimal places cannot be of different type than int and not equal to 0! ")
                        elif digit_first.lstrip("-").replace('.','',1).isdigit() and digit_second.lstrip("-").replace('.','',1).isdigit() and digit_first.count("-")<=1 and digit_second.count("-")<=1:
                            digit_first = float(digit_first)
                            digit_second = int(digit_second)
                            print(f"Rounding: {digit_first} with {digit_second} decimal places = {round(digit_first,digit_second)} ")
                        else: print("\nWrong value! Please, input either float (e.g. 1.1) or integer (e.g. 1) value! Thank you! ")
                continue
            elif operation == "auto":
                while True:
                    print("""                          WELCOME TO AUTO MODE
                                                    Enter command you like with the spaces 

                                                      example:digit_operation_digit
              _______________________________________________________________________________________________________________
operation -->|   Operations:    | Perfect square of x: x_*p  | Rounding x by y               | Random: from x to y           | 
more info -->|     +-/*%**//    |                            | y is number of decimal places | x,y set range                 | 
exmaple   -->|example:1 + 1 = 2 |     example:4 *p = 16      | example:1.12345 r 3 = 1.123   | example:0 rnd 100 = random num| 
             *****************************************************************************************************************
""")
#operations = ('+','-','/','*','//','%','**','*s','r','rnd','end')
                    command = input("Enter command: ") 
#                    if str(operations) in command == False:
#                       print("Your symbol doesn't match available opeartions. Try again")
#                        continue
                        #print(command_check)
                        #print(len(command_check))
                    for command in operations:
                        if command == operations[0]:
#                        command_check=command.split()
 #                       if command_check in operations:
                            print("Success")
                    else: print("check your input")
#                        sym=command_check[1]
#                        first_digit=float(command_check[0])
#                        second_digit=float(command_check[2])
#                        if sym == '+':
#                            print(f"Result of Addition {first_digit} + {second_digit} = {first_digit+second_digit}")
#                        elif sym == '-':
#                            print(f"Result of Substraction {first_digit} - {second_digit} = {first_digit-second_digit}")
#                        elif sym == '*':
#                            print(f"Result of Multiplication {first_digit} * {second_digit} = {first_digit*second_digit}")
#                        elif sym == '/':
#                            if second_digit == 0:
#                                print("You cannot devide by 0. Try different")
#                            else:
#                                print(f"Result of Devision {first_digit} / {second_digit} = {first_digit/second_digit}")
#                        elif sym == '//':
#                            if second_digit == 0:
#                                print("You cannot devide by 0. Try different")
#                            else:
#                                print(f"Result of Devision {first_digit} // {second_digit} = {first_digit//second_digit}")
#                        elif sym == '%':
#                            if second_digit == 0:
#                                print("You cannot devide by 0. Try different")
#                            else:
#                                print(f"Result of Devision {first_digit} % {second_digit} = {first_digit%second_digit}")
#                        elif sym == '**':
#                            print(f"Power of {first_digit} to {second_digit} = {first_digit**second_digit}")
#                    elif command_check[0].lstrip("-").replace('.','',1).isdigit() and command_check[1]=='*p' and len(command_check)==2:
#                        first_digit=float(command_check[0])
#                        print(f"Square power of {first_digit} = {first_digit**first_digit}")
#                    elif command_check[0].lstrip("-").replace('.','',1).isdigit() and command_check[1]=='rnd' and command_check[2].lstrip("-").replace('.','',1).isdigit() and len(command_check)==3:
#                        sym=command_check[1]
#                        first_digit=float(command_check[0])
#                        second_digit=float(command_check[2])
#                        if first_digit < second_digit:
#                            print(f"Random num between {first_digit} and {second_digit} is {random.randrange(first_digit,second_digit)}")
#                        elif first_digit==second_digit:
#                            print("Numbers are equal")
#                        else:
#                            print(f"Random num between {second_digit} and {first_digit} is {random.randrange(second_digit,first_digit)}")
#                    elif command_check[0].isdigit() and command_check[1]=='r' and command_check[2].isdigit() and len(command_check)==3:
#                        if int(second_digit)==False:
#                            print("Number of decimal places can only be of integer value. Try again")
#                        else:
#                            first_digit=float(command_check[0])
#                            second_digit=int(command_check[2])
#                            print(f"Rounding: {first_digit} with {second_digit} decimal places = {round(first_digit,digit_second)} ")
#                    #elif len(command_check)==2 and command_check[0].isdigit() and command_check[1].isalnum()==False:  
#                break
            print(f"{user_name_inp.capitalize()}, Thank you for using our calculator!")
            break
    else: print("It is not name")
    continue
