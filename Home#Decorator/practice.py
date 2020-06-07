import time
from functools import wraps 

def power_entry(y):
    def decorating_func(func):
        def wrapper(x):
            t1=time.time()
            t2=time.time()
            return f"""
            Result is {x**y}
            process time: {t2-t1}
            """
        return wrapper
    return decorating_func


@power_entry(10)
def square_num(x):
    x = x**x
    return f"{x}" 

print(square_num(2))



def lowercase(value):
    import time
    def add_time(func):
        print(value)
        def wrapper(*args, **kwargs):
            print("At the start")
            t1 = time.time()
            return_val = func().lower()
            t2 = time.time()
            print("After")
            print(f"Total time: {t2-t1}")
            return return_val
        return wrapper
    return add_time

@lowercase("OOoooOO")
def uppercase():
    value = ("OOoooOO")
    return value.upper()

print(uppercase())

"""add_time = lowercase(value)
uppercase = lowercase(value)(uppercase)"""


def explainer(func):

    def wrapper(*args, **kwargs):
        print(help(func))
        print(dir(func))
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


class Upper:

    def __init__(self, lists):
        if type(lists) == list:
            for i in lists:
                if i.isupper():
                    self.lists = lists
        else:
            raise ValueError("Should contains upper str only")
    @explainer
    def lower(self):
        for i in range(len(self.lists)):
            self.lists[i] = self.lists[i].lower()
        return self.lists

    def __str__(self):
        return f"{self.lists}"

    def __repr__(self):
        return f"{self.lists}"


r = Upper(["I", "G", "H"])
"""help(Upper.__doc__)
help(Upper)
help(Upper.__init__)"""
print(r.lower.__doc__)
print(r.lower())

print()
print()
print()


def security_check(func):
    def wrapper(*args, **kwargs):
        password_check = input("old password: ")
        if password_check == user.password:
            print("check passed")
            print(args)
            print(kwargs)
            func(*args, **kwargs)
        else: raise ValueError("Wrong")
        return "Sucess"
    return wrapper

class Admin_User():

    def __init__(self, name = 's', password = 'q'):
        self.__name = name
        self.__password = password

    def get_name(self):
        print("get_name")
        return self.__name

    def get_password(self):
        print("get_password")
        return self.__password

    def set_name(self, name):
        print("set_name")
        self.__name = name
 
    @security_check
    def set_password(self, password):
        print("set_password")
        self.__password = password


    password = property(get_password, set_password)
    user_name = property(get_name, set_name)

user = Admin_User()
user.password = 's'
print(user.password)