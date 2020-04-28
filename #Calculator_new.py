#Calculator
import random
import math
import collections
#menu_operations = OrderedDict()
menu_operations = {
'+':"\nAddition ",
'-':"\nSubstraction ",
'/':"\nDivision ",
'*':"\nMultiplication ",
'//':"\nFloor Division ",
'%':"\nModulus ",
'**':"\nExponent ",
'r':"\nRounding ",
'rnd':"\nRandomizer "
}
def validate(value):
    return value.isdigit()
def convertation(value):
    if validate(value) == True:
        return float(value)
    return None
def addition(x,y):
    if x is None or y is None:
        return print("You have wrong input ")
    return x + y
def substraction(x,y):
    if x is None or y is None:
        return print("You have wrong input ")
operations = {
'+': addition,
'-': substraction
}
print (""" Hello, calculator welcomes you! """)

def name_check(name):
    while True:
        user_name = input("Please, enter your name: ")
        if user_name.isalpha():
            user_name = user_name.capitalize()
            return user_name.capitalize()
        else:
            print("If that is your name I feel sorry for you :-) But I can call you R2D2:   ")
            name_check = input("\nIf you like to be called R2D2 enter '2' or '1' to try again:   ")
            if name_check == '2':
                return "R2D2"
            elif name_check == '1':
                continue
            else:
                print("You are definitely robot! So I will call you R2D2")
                return "R2D2"
        break

name = name_check(name)
print(f"\nNice to meet you, {name}! Welcome to main menu"
for key, value in menu_operations.items():
    print(k,"-",v)