list=(1,2,3,4)
def oops(x):
    print(list[x])
    raise IndexError('Sorry, you got index error')
def calls_oops():
    try:
        x = input('we have list with 1,2,3,4 elements. try to reach index out of it ')
        oops(list[int(x)])
    except IndexError:
        print("Range successfuly breached! ")
    else: print('no luck.')
    finally:
        print("that is how we work")
calls_oops()