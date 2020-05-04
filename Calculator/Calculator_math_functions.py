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