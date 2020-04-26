from operator import add, sub, mul, truediv, mod, pow, floordiv
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.pow,
    '//': operator.floordiv,
}
command = ''
first_digit = 1
second_digit = 1
command_check = command.split