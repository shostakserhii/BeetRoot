command = ''
while True:
    command = input("Please, input operation: ")
    if command == "end":
        break    
    else: print("The result is: " + str(eval(command)))
    continue