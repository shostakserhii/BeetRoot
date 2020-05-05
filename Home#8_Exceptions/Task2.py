def task(a,b):
    try:
        a = float(a)
        b = float(b)
        a*a/b
    except ValueError:
        print(f"You entered wrong value, '{a}', '{b}' are not digits, are they? ")
    except ZeroDivisionError:
        print(f"You cannot device either {a} or anything else by 0, sorry for the truth")
    else: 
        return a*a/b
a = input("Input A: ")
b = input("Input B: ")
if task(a,b).is_integer():
        print(int(task(a,b)))
print(task(a,b))