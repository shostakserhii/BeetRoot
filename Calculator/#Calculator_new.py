#Calculator
import random
import collections
from operator import pow, truediv, mul, add, sub 
first_digit = None
second_digit = None
name = str
menu_operations = {
'"+"':"for addition",
'"-"':"for substraction",
'"/"':"for division",
'"*"':"for multiplication",
'"//"':"for floor division",
'"%"':"for modulus",
'"**"':"for exponent",
'"r"':"for rounding",
'"rnd"':"for randomizer",
'"end"':"to finish working with calculator",
'"am"':"to enter automode"
}
operations = ("+", "-", "/", "*", "//", "%", "**", "r", "rnd", "end", "auto")
def name_check(name):
    while True:
        name = input("\nPlease, enter your name: ")
        if name.isalpha():
            return name.capitalize()
        else:
            print('\nIf that is your real name I don\'t envy you! \nBut if you want I can call you R2D2 ')
            x = input("\nCall R2D2 - 1; or press 2 to try again: ")
            if x == '1':
                return "R2D2"
            elif x == '2':
                continue
            else: 
                print('\nYou are definitely robot so I will call you R2D2')
                return "R2D2"
        continue
def validate(value):
    if value.lstrip("-").replace('.','',1).isdigit() and value.count("-")<=1:
        return True
def convertation(value):
    if validate(value) == True:
        if value == int(value):
            return int(value)
        value == float(value)
        return float(value)
    return None
def additing(x,y):
    first = convertation(x)
    second = convertation(y)
    if first is None or second is None:
        return None
    return first + second
def substraction(x,y):
    first = convertation(x)
    second = convertation(y)
    if first is None or second is None:
        return None
    return first - second
def division(x,y):
    first = convertation(x)
    second = convertation(y)
    if second == 0:
        return print("You cannot divide by zero")
    elif first is None or second is None:
        return None
    return first / second
def division_auto (x,y):
    if y == 0:
        return print("You cannot divide by zero")
    if y is None or x is None:
        return None
    return x / y
def multiplication(x,y):
    first = convertation(x)
    second = convertation(y)
    if first is None or second is None:
        return None
    return first * second
def floor_division(x,y):
    first = convertation(x)
    second = convertation(y)
    if second == 0:
        return print("You cannot divide by zero")
    elif first is None or second is None:
        return None
    return first // second
def floor_division_auto(x,y):
    if y == 0:
        return print("You cannot devide by 0")
    return x // y  
def modulus(x,y):
    first = convertation(x)
    second = convertation(y)
    if second == 0:
        return print("You cannot divide by zero")
    elif first is None or second is None:
        return None
    return first % second
def modulus_auto(x,y):
    if y == 0:
        return print("You cannot modulo by 0")
    return x % y  
def exponent(x,y):
    first = convertation(x)
    second = convertation(y)
    if first != None and second == int(second):
        return first ** second
    return None
def rounding(x,y):
    first = convertation(x)
    second = convertation(y)
    if first != None and second == int(second):
        return round(first,int(second))
    return None
def rounding_auto(x,y):
    if y != int(y):
        return print("Number of decimal places should be integer")
    return round(x,int(y))
def randoming(x,y):
    first = convertation(x)
    second = convertation(y)
    if first is None or second is None:
        return None
    elif first > second:
        return random.randrange(second, first)
    elif first < second:
        return random.randrange(first, second)
def randoming_auto(first,second):
    if first > second:
        return random.randrange(second, first)
    elif first < second:
        return random.randrange(first, second)
############################## AUTOMODE FUNCTION ##################################
operations_auto = {
'+':add,
'-':sub,
'/':division_auto,
'*':mul,
'%':modulus_auto,
'rnd':randoming_auto,
'r':rounding_auto,
'**':pow,
'//':floor_division_auto
}
def command_validation(command):
    operation = get_operation(command)
    if operation is None:
        return None   
    left, symbol, right = command.partition(operation)
    if validation_num(left) and validation_num(right): 
        for symbol in operations_auto.keys():
            if operation == symbol: 
                if operation == "/" or operation == '//' or operation =='%':
                    if right == 0:
                        return print(f"Sorry, {name}, but you cannot divide by 0")
                    else:
                        left = float(left)
                        right = float(right)
                        return operations_auto[symbol](left,right)
                left = float(left)
                right = float(right)
 #               if operations_auto[symbol](left,right).isinstance():
 #                   return int(operations_auto[symbol](left,right))
                return operations_auto[symbol](left,right) 
    return None
def validation_num(num):
    return num.strip().lstrip("-").strip().replace('.','',1).isdigit()
def get_operation(command):
    for operation in operations:
        if operation == '//' and operation in command:
            return operation
        elif operation == '**' and operation in command:
            return operation
        elif operation == 'rnd' and operation in command:
            return operation
    for operation in operations: 
        if operation in command.lstrip('-'):
            return operation
    return None
####################################################################################
print ("HELLO, PyCULATOR WELCOMES YOU!".center(53))
name = name_check(name)
print(f"\nNice to meet you, {name}! ")
while True:
    delimiter = '+' + '-' * 53 + '+'
    print("MAIN MENU".center(53))
    print(delimiter)
    for index, item in menu_operations.items():
        index_length = abs(len(index) - 8)
        line_length = abs((10 + len(index) + index_length + len(item)) - len(delimiter))
        print('| Enter: ' + index + ' '*index_length + item + ' '* line_length + '|')
    print(delimiter)
    operation = input("\nEnter symbol to choose operation: ")
    if operation not in operations:
        print("Wrong input, try again")
    elif operation == "end":
        print("\nThank you for using PyCulator")
        break
    elif operation == operations[0]:
        while True:
            result = additing(input("Enter first digit: "), input("Enter second digit: "))
            if result is None:
                print("Try again since you entered wrong elements which cannot be added")
                continue
            else: print(f"The result of addition = {result} ") 
            break
    elif operation == operations[1]:
        while True:
            result = substraction(input("Enter first digit: "), input("Enter second digit: "))
            if result is None:
                print("Try again since you entered wrong elements which cannot be subsctracted")
                continue
            else: print(f"The result of addition = {result} ") 
            break
    elif operation == operations[2]:
        while True:
            result = division(input("Enter first digit: "), input("Enter second digit: "))
            if result is None or result == "You cannot divide by zero":
                print("Try again since you entered wrong elements which cannot be divided")
                break
            else: print(f"The result of division = {result} ") 
            break
    elif operation == operations[3]:
        while True:
            result = multiplication(input("Enter first digit: "), input("Enter second digit: "))
            if result is None:
                print("Try again since you entered wrong elements which cannot be multiplied")
                continue
            else: print(f"The result of multiplication = {result} ") 
            break
    elif operation == operations[4]:
        while True:
            result = floor_division(input("Enter first digit: "), input("Enter second digit: "))
            if result is None or result == "You cannot divide by zero":
                print("Try again since you entered wrong elements which cannot be floor divided")
                continue
            else: print(f"The result of floor division = {result} ") 
            break
    elif operation == operations[5]:
        while True:
            result = modulus(input("Enter first digit: "), input("Enter second digit: "))
            if result is None or result == "You cannot divide by zero":
                print("Try again since you entered wrong elements")
                continue
            else: print(f"The result of modulus = {result} ") 
            break
    elif operation == operations[6]:
        while True:
            result = exponent(input("Enter digit: "), input("Enter power: "))
            if result is None:
                print("Try again since you entered wrong elements")
                continue
            else: print(f"The result of exponent = {result} ") 
            break
    elif operation == operations[7]:
        while True:
            result = rounding(input("Enter digit: "), input("Enter the integer number of decimal places: "))
            if result is None:
                print("Try again since you entered wrong elements.")
                continue
            else: print(f"The result of rounding = {result} ") 
            break
    elif operation == operations[8]:
        while True:
            result = randoming(input("Set the beginning or range "), input("Enter the end of range "))
            if result is None:
                print("Try again since you entered wrong elements.")
                continue
            else: print(f"The result of rounding = {result} ") 
            break    
    elif operation == operations[-1]:
        while True:
            print(f"""
                                {name}, you entered AutoMode*

*Arithmetic:whole command

**Random number: 'rnd' for random number or '1 rnd 100' for range

***Rounding: separate number and number of decimal places you need with 'r' sign - 0.1234 r 2
""")
            command = input("Enter full command: ")
            if command_validation(command) is None:
                print("Wrong input") 
                break
            elif command_validation(command).is_integer():
                print("The result = " +str(int(command_validation(command))))
                break
            print("The result = " +str(command_validation(command)))
            break