class Test:

    def __init__(self, var):
        self.__var = var

    def get_var(self):
        print("get")
        return self.__var

    def set_var(self, var):
        print("set")
        self.__var = var

    our_property = property(get_var, set_var)

t = Test(1)
print(t.our_property)
t.our_property = 10
print(t.our_property)

class Test2:
    def __init__(self, var):
        self.__var = var

    @property
    def get_var(self):
        print("get")
        return self.__var
    @get_var.setter
    def set_var(self, var):
        print("set")
        self.__var = var


x = Test2(5)
print(x.get_var)
x.set_var = 10
print(x.get_var)
print()
print()
print("Static Method/Class Method")


class Stat_test():

    def __init__(self, x):
        self.x = x

    @staticmethod
    def static_method(self):
        if type(self.x) is str: 
            return f"static method result: {self.x.lower()}"
        raise ValueError("should be str")

    @classmethod
    def class_method(cls,x):
        print("Class method result:")
        return cls(x.lower())

    def __str__(self):
        return self
    def __repr__(self):
        return self


value = ("UPPER")
test = Stat_test.class_method(value)

print(test.x)
print(test.static_method(test))