from contextlib import contextmanager
import os


@contextmanager
def count_upper(object):
    our_file = open(object)
    full = our_file.read()
    for i in full:
        if i.isupper():
            print(f"{i} Hello!")
    yield our_file
    print(full)

with count_upper('myfile.txt') as mf:
    print(mf.read())


class Exampler:

    def __init__(self, value):
        self.value = value
        self.__local_value = value[:]
    
    def __enter__(self):
        print("__enter__")
        return self.value

    def __exit__(self, type, value, traceback):
        print("__exit__")
        self.value = self.__local_value[:]

newlist = Exampler(['a', 'b', '1', 4])
print(newlist.value)
with newlist as f:
    f.append(5)
    print(f)
    print(newlist.value)
print(newlist.value)


class Count_upper:

    def __init__(self, filename):
        if os.path.exists(filename):
            self.__filename = open(filename)
        else:
            raise FileNotFoundError
        self.counter = 0
    
    def __enter__(self):
        full_file = self.__filename.read()
        for i in full_file:
            if i.isupper():
                yield i

    def __exit__(self, type, value, traceback):
        self.__filename.close()

"""with Count_upper('myfile.txt') as mf:
    print(list(mf))"""

"""@contextmanager
def count_upper(object):
    our_file = open(object)
    full = our_file.read()
    for i in full:
        if i.isupper():
            print(i)
    yield our_file
    print(full)"""

class Own:

    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)

    def __enter__(self):
        yield self.func
    
    def __exit__(self, type, value, traceback):
        self.args.close()
        

@Own
def count_upper2(object):
    our_file = open(object)
    full = our_file.read()
    for i in full:
        if i.isupper():
            print(i)
    yield our_file
    print(full)
    
with count_upper2('myfile.txt') as mf:
    print(mf.read())