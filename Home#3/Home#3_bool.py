#Task1
sample_string = input("Enter word: ")
if sample_string.strip().isalpha():
    if len(sample_string.strip())<2:
        print("Try longer word")
        print()
    elif len(sample_string.strip())>=2:
        print(sample_string.strip()[:2]+sample_string.strip()[-2:])     
else : print("Come on! u failed even to write a word!?")

#Task2(validate phone)
phone_num = input("Enter phone number: ")
if phone_num.isdigit() and len(phone_num)==10 :
    print("Nice job! Here is your phone number: "+phone_num)
elif phone_num.isdigit() == False:
    print("Try to type 10 digits")

#Task3 (The name check via capilize and lower)
name_memory = "Serhii" 
name = input("Type in your name, please: ")
if name_memory == name.capitalize():
    print("Thank you for authorization! ")
else: print("Sorry, authorization failed!. Try again")

#Task3 (The name check via .lower)
name_memory = "serhii" 
name = input("Type in your name, please: ")
if name_memory == name.lower():
    print("Thank you for authorization! ")
else: print("Sorry, authorization failed!. Try again")