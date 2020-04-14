#Bool
#print(True, type(True))
#print(type(1.34) == float)
print(True == 1)
print(int(True))
print('{:O<10}'.format('test'))
print('{:S>20}'.format('Serhii') )
print('{:^20}'.format('Serhii'))
print('{:<10}'.format('open'))
print('{:>20}'.format('open'))
print('{:n>20}'.format('not open'))
test_text = "evadakedavra"
print('{:_>20}'.format(test_text))
print('{:f}'.format(3.141592653589793))
print('{:_>16.4f}'.format(0.12345678))
text =  " Hello! Today is {day}, month is {month}"
print(text.format(day='Monday',month='March'))
