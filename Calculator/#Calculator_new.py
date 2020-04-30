#Calculator
import random
import collections
from operator import pow, truediv, mul, add, sub 
#menu_operations = OrderedDict()
first_digit = None
second_digit = None
name = str
operator = ''
menu_operations = {
'+':"for Addition ",
'-':"for Substraction ",
'/':"for Division ",
'*':"for Multiplication ",
'//':"for Floor Division ",
'%':"for Modulus ",
'**':"for Exponent ",
'r':"for Rounding ",
'rnd':"for Randomizer ",
'Example: ': "enter '+' to proceed with addition",
'end':" to finish working with calculator",
'auto':" to enter automode"
}
operations = ("+", "-", "/", "*", "//", "%", "**", "r", "rnd", "end", "auto")
def name_check(name):
    while True:
        name = input("Please, enter your name: ")
        if name.isalpha():
            return name.capitalize()
        else:
            print('Wrong input')
            continue
def validate(value):
    if value.lstrip("-").replace('.','',1).isdigit() and value.count("-")<=1:
        return True
def convertation(value):
    if validate(value) == True:
        value = float(value)
        return value
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
'/':truediv,
'*':mul,
'%':modulus_auto,
'rnd':randoming_auto,
'r':rounding_auto,
'**':pow,
'//':floor_division_auto
}
'''def automode(value):
    if value.strip('-').replace('.','').isdigit():
        return float(value)
    for symbol in operations_auto.keys():
        left, symbol, right = value.partition(symbol)
        if symbol in operations_auto:
            return operations_auto[symbol](left,right)'''
def command_validation(command):# - це перевірка комнади в *автомоді*
    left, symbol, right = command.split() # here I am making split cause 
    #for some reason I cannot make partition function to work - it awlays gives me 'str' object has no attribute 'partition'
    if left.lstrip("-").replace('.','',1).isdigit() and right.lstrip("-").replace('.','',1).isdigit() and symbol in operations: #перевіряю чи тапл відповідає вимогам
        for c in operations_auto.keys():#лупаю ключі і розділяю фразу за left|operation|right щоб переконатись що декілька операцій теж могли ранитись
            left, right = command.split(c)
            left = float(left)
            right = float(right)
            return operations_auto[c](left,right)
    return None          
####################################################################################


print (""" Hello, calculator welcomes you! """)
name = name_check(name)
print(f"\nNice to meet you, {name}! Welcome to main menu")
while True:
    for k, v in menu_operations.items():
        print(k,v)
    operation = input("Enter symbol: ")
    if operation not in operations:
        print("Wrong input, try again")
    elif operation == "end":
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
                continue
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
            command = input("Enter command: ")
            if str(command_validation(command)) == None:
                print("Wrong input")
            print("The result = " +str(command_validation(command)))
            break