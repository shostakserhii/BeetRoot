class OnlyDigit(Exception):

    def __init__(self,msg):
        self.msg = msg
    

#log = open("logs.txt", "a") 
try:
    number = input("Number: ")
    if number.isalpha():
        raise OnlyDigit(f"Number cannot contain letters")

except OnlyDigit as e:
    with open("logs.txt","a") as log:
        log.write("\n")
        log.write(str(e))
        print(e)
finally:
    log.close()
