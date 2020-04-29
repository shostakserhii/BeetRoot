#The greeting program.\
print('Task 1: The greeting program. e.g. “Good day <name>! <day> is a perfect day to learn some python.” ')
name = 'Serhii'
x = 0
day0 = 'Monday'
day1 = 'Tuesday'
day2 = 'Wednesday'
day3 = 'Thursday'
day4 = 'Friday'
day5 = 'Saturday'
day6 = 'Sunday'
print()
print(name + ' has '+day0+' today')
print(name + ' has '+day1+' today')
print(name + ' has '+day2+' today')
print(name + ' has '+day3+' today')
print(name + ' has '+day4+' today')
print(name + ' has '+day5+' today')
print(name + ' has '+day6+' today')
print()
print("Task 2: Manipulate strings using first and last name: ")
print()
task2 = """Hello,
Shostak
Serhii\n"""
print(task2)
print()
print("Hello,\nShostak\nSehii")
print()
print(type(task2))
print()
name = "serhii"
print(name.count('i'))
print(name.count('S'))
print(name.upper())
print(name)
name = name.upper()
print()
print(name)
print("Number of 'S' letter:", name.count('S'))
name = name.replace('ERHII',"erhii")
print(name)
print(name.index('S'))
print()
print(name[0],name[1],name[2],name[3],name[4],name[5])
print(name[-6:])
first_name = "Serhii"
last_name = "Shostak"
middle_name = "Oleksiyovich"
print(f'Last name is: {last_name},\nFirst name is: {first_name},\nMiddle name is: {middle_name}')
initials = last_name[0] + first_name[0]
print(f"Hello World, your" + ' ' + initials)
greeting = 'Hello world, yours {}'
print(greeting.format(initials))
print()
print("Task#3 Python show me your math skills! :")
print()
a = 5
b = 10
print(f'Addition of {a} + {b} = {a+b}')
print(f'Subtraction of {a} - {b} = {a-b}')
print(f'Division of {a} / {b} = {a/b}')
print(f'Multiplication of {a} * {b} = {a*b}')
print(f'Modulus of {a} % {b} = {a%b}')
print(f'Exponent (Power) of {b} to {a} = {b**a}')
print(f'Floor division of {b} with {a} = {b//a}')
