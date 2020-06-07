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

    def __init__(self, x = "STAT_TEST"):
        self.x = x
    
    @staticmethod
    def static_method(value):
        if type(value) is str: 
            return f"{value.lower()}"
        raise ValueError("should be str")

    @classmethod
    def class_method(cls,x):
        return cls(x.lower())
    
    def __str__(self):
        return self.x
    def __repr__(self):
        return self.x



st = Stat_test
print(st.static_method("UPPPER"))

val = ("LOWER")
test  = Stat_test.class_method(val)
print(test)



