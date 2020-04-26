#Calculator_new
# variables we work with
first_digit = 0
second_digit = 0
symbol = ''
error = ("You made an error. Check format and try again")
while True:
    print("""                                           WELCOME TO AUTO MODE
                                                Enter command you like with the spaces 

                                                    example:digit_operation_digit
            _______________________________________________________________________________________________________________
operation -->|   Operations:    | Perfect square of x: x_*p  | Rounding x by y               | Random: from x to y           | 
more info -->|     +-/*%**//    |                            | y is number of decimal places | x,y set range                 | 
exmaple   -->|example:1 + 1 = 2 |     example:4 *p = 16      | example:1.12345 r 3 = 1.123   | example:0 rnd 100 = random num| 
            *****************************************************************************************************************
""")
    command = input("Enter command: ") 
    command_check = command.split()
    if command == 'end':
        print("Thank you for using our calculator!")
        break
    #print(command_check)
    #print(len(command_check))
    elif command_check[0].lstrip("-").replace('.','',1).isdigit() and command_check[1].isalnum()==False and command_check[2].lstrip("-").replace('.','',1).isdigit() and len(command_check)==3:
        sym=command_check[1]
        first_digit=float(command_check[0])
        second_digit=float(command_check[2])
        if sym == '+':
            print(f"Result of Addition {first_digit} + {second_digit} = {first_digit+second_digit}")
        elif sym == '-':
            print(f"Result of Substraction {first_digit} - {second_digit} = {first_digit-second_digit}")
        elif sym == '*':
            print(f"Result of Multiplication {first_digit} * {second_digit} = {first_digit*second_digit}")
        elif sym == '/':
            if second_digit == 0:
                print("You cannot devide by 0. Try different")
            else:
                print(f"Result of Devision {first_digit} / {second_digit} = {first_digit/second_digit}")
        elif sym == '//':
            if second_digit == 0:
                print("You cannot devide by 0. Try different")
            else:
                print(f"Result of Devision {first_digit} // {second_digit} = {first_digit//second_digit}")
        elif sym == '%':
            if second_digit == 0:
                print("You cannot devide by 0. Try different")
            else:
                print(f"Result of Devision {first_digit} % {second_digit} = {first_digit%second_digit}")
        elif sym == '**':
            print(f"Power of {first_digit} to {second_digit} = {first_digit**second_digit}")
    elif command_check[0].lstrip("-").replace('.','',1).isdigit() and command_check[1]=='*p' and len(command_check)==2:
        sym=command_check[1]
        first_digit=float(command_check[0])
        print(f"Square power of {first_digit} = {first_digit**first_digit}")
    elif command_check[0].lstrip("-").replace('.','',1).isdigit() and command_check[1]=='rnd' and command_check[2].lstrip("-").replace('.','',1).isdigit() and len(command_check)==3:
        import random
        sym=command_check[1]
        first_digit=float(command_check[0])
        second_digit=float(command_check[2])
        if first_digit < second_digit:
            print(f"Random num between {first_digit} and {second_digit} is {random.randrange(first_digit,second_digit)}")
        elif first_digit==second_digit:
            print("Numbers are equal")
        else:
            print(f"Random num between {second_digit} and {first_digit} is {random.randrange(second_digit,first_digit)}")
    elif command_check[0].isdigit() and command_check[1]=='r' and command_check[2].isdigit() and len(command_check)==3:
        if int(second_digit)==False:
            print("Number of decimal places can only be of integer value. Try again")
        else:
            first_digit=float(command_check[0])
            second_digit=int(command_check[2])
            print(f"Rounding: {first_digit} with {second_digit} decimal places = {round(first_digit,digit_second)} ")
    else:
        print("Your symbol doesn't match available opeartions. Try again")
    #elif len(command_check)==2 and command_check[0].isdigit() and command_check[1].isalnum()==False:  
        continue
