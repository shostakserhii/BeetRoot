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