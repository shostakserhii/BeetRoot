from operator import pow, truediv, mul, add, sub  
x = ("-2--2")
l=list()
def minus(line):
    i = 0
    n=0
    x = list()
    y= list()
    while True:
        if i < len(line):
            if line[i]=='-' and [i]==0:
                x.append(line[i])
                print(x)
minus(x)