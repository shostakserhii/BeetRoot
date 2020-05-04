def command_validation(command):
    operation = get_operation(command)
    if operation is None:
        return None   
    left, symbol, right = command.partition(operation)
    if validation_num(left) and validation_num(right): 
        for symbol in operations_auto.keys():
            if operation == symbol: 
                if operation == "/" or operation == '//' or operation =='%':
                    if right == 0:
                        return print(f"Sorry, {name}, but you cannot divide by 0")
                    else:
                        left = float(left)
                        right = float(right)
                        return operations_auto[symbol](left,right)
                left = float(left)
                right = float(right)
 #               if operations_auto[symbol](left,right).isinstance():
 #                   return int(operations_auto[symbol](left,right))
                return operations_auto[symbol](left,right) 
    return None
