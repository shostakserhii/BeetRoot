import math
#Calculator_new
# variables we work with 
error = ("You made an error. Check format and try again")
first_digit = 1
second_digit = 1
symbol = ''
command = ''
opers = {
"+" : sum(first_digit,second_digit),
"-" : print("Substraction")
        }
command = input("Enter the preferable operation: ")
command_check = command.split()
if command_check[0].lstrip("-").replace('.','',1).isdigit() and command_check[1].isalnum()==False and command_check[2].lstrip("-").replace('.','',1).isdigit() and len(command_check)==3:
    symbol = command_check[1]
    first_digit=float(command_check[0])
    second_digit=float(command_check[2])
    if symbol == '+':
        print(opers["+"])
else:
    print('Mistake')