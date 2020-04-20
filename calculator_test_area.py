operation = input("operation :")
if operation != 'end':
    if operation == "a":
        while True:
            command = input("Enter command you like with the spaces (e.g. 1 + 1)")
            command_check = command.split()
            print(command_check)
            print(len(command_check))
            if command_check[0].isdigit() and command_check[1].isalnum()==False and command_check[2].isdigit() and len(command_check)==3:
                sym=command_check[1]
                first_digit=float(command_check[0])
                second_digit=float(command_check[2])
                if sym == '+':
                    print(f"Result of Addition {first_digit} + {second_digit} = {first_digit+second_digit}")
                elif sym == '-':
                    print(f"Result of Substraction {first_digit} - {second_digit} = {first_digit-second_digit}")
                elif sym == '*':
                    print(f"Result of Multiplication {first_digit} * {second_digit} = {first_digit*second_digit}")
                else:
                    print("It is another symbol")
            else:
                print("Your input has wrong format")    
    else:
            print("Wrong operation")
else: "Wrong opperation"