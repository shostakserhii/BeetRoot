while True:
    digit_first = input("Input digit or enter 'end' to quit to menu: ")
    if digit_first.strip("-").replace('.','',1).isdigit():
        print('it is digit')
    elif digit_first == 'end':
        break
    else: print("Wrong value")
    continue

if operation=='+':
                print(f"{user_name_inp.capitalize()}, you chose Addition for which you need 2 operands ")
                print(user_name_inp.capitalize()+", please enter left hand operand: ")
                digit_first = (input())
                digit_first_check = ''
                if float(digit_first_check).isdigit:
                    digit_first_check == float(digit_first)
                    print(user_name_inp.capitalize()+", please enter right hand operand:")
                    digit_second = (input(f"{digit_first_check} + "))
                    digit_second_check = float(digit_second)
                    if type(digit_first_check)==float and type(digit_second_check)==float:
                        print(f"Addition: {digit_first_check} + {digit_second_check} = {digit_first_check+digit_second_check} ")
                    else: 
                        print("It doesn't look like digits I can work with! Please, input either float (1.0) or integer (1) value! Thank you! ")
                else:print("You typed not number")

if operation=='+':
    print(f"{user_name_inp.capitalize()}, you chose Addition for which you need 2 operands ")
    print(user_name_inp.capitalize()+", please enter left hand operand: ")
    while True:
    digit_first = input("Input first digit or enter 'end' to quit to menu: ")
    digit_second = input("Input second digit or enter 'end' to quit to menu: ")
    if digit_first.strip("-").replace('.','',1).isdigit() and digit_second.strip("-").replace('.','',1).isdigit()
        digit_first = float(digit_first)
        digit_second = float(digit_second)
        print(f"Addition: {digit_first_check} + {digit_second_check} = {digit_first_check+digit_second_check} ")
    elif digit_first == 'end':
        break
    else: print("Wrong value")
    continue