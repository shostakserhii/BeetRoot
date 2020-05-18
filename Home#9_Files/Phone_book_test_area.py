import json
import sys

json_file = open('json_buffer')
try:
    phonebook = json.load(json_file)
except json.decoder.JSONDecodeError:
    phonebook = []
json_file.close()

##################################################
#           VALIDATIONS                          #
##################################################
def validation_num(phone):
    if phone.isdigit():
        return phone
    print('Incorrect input. Try again')


def validation_name(name):
    if name.isalpha():
        return name
    print('Incorrect input. Try again')

def validation(inputing, category):
    if category == 'phone':
        if inputing.isdigit():
            return inputing
        return None
    elif category is first_name or category is second_name or category is full_name or category is city: 
        if inputing.isalpha():
            return inputing
    print('Incorrect input. Try again')
    return None

##################################################
#           VARIABLES                            #
##################################################
first_name = 'first name'
second_name = 'second name'
full_name = 'full name'
phone = 'phone'
city= 'city'

dict_json = {
'first name':'',
'second name':'',
'full name':'',
'phone':'',
'city':''
}

search ={
'first name':first_name,
'second name':second_name,
'full name':full_name,
'phone':phone,
'city':city
}
####################################################
#               BODY FUNCTIONS                     #
####################################################

def user_add_new():
    first_name = validation_name(input("Please, enter first name: ").capitalize())
    second_name = validation_name(input("Please, enter second name: ").capitalize())
    full_name = first_name.capitalize() + " " + second_name.capitalize()
    phone_num = validation_num(input("Please, enter phone number: "))
    city = validation_name(input("Input the city: "))
    new_add = dict_json.copy()
    new_add['first name'] = first_name.capitalize()
    new_add['second name'] = second_name.capitalize()
    new_add['full name'] = full_name
    new_add['phone'] = phone_num
    new_add['city'] = city.capitalize()
    phonebook.append(new_add)


def k_v(item):
    for keys,values in item.items():
        print(f"{keys}: {values}")


def search(key, value):
    value = validation((input(f"Enter {str(key)} you want to find")),value)
    if value is None:
        return print("wrong input") 
    else:
        i = 0
        for item in phonebook:
            if item[key] == value:
                i+=1
                print(f"\nAbonent #{i}\n")
                k_v(item)
                what_to_do(item)
        if i == 0:
            return print("No results found")

#############################################################
#                   WHAT TO DO                              #
#############################################################        
def delete(phone):
    for item in phonebook:
        if item['phone']==phone:
            phonebook.remove(item)


def update(phone):
    for item in phonebook:
        if item['phone']==phone:
            item['first name'] = input(f"Current first name is {item['first name']}. Enter name you want it to be changed to:")
            item['second name'] = input(f"Current first name is {item['second name']}. Enter name you want it to be changed to:")
            item['full name'] = item['first name'].capitalize() + " " + item['second name'].capitalize()
            item['city'] = input(f"Current first name is {item['city']}. Enter name you want it to be changed to:")

            
def what_to_do(item):
    choice = input("""What do you want to do with abonent:
                    d - delete
                    u - update
                    c - continue seraching
    """).strip().lower()
    if choice == 'd':
        phonebook.remove(item)
        return print("Abonent is erased")
    elif choice == 'u':
            item['first name'] = input(f"Current first name is {item['first name']}. Enter name you want it to be changed to:")
            item['second name'] = input(f"Current first name is {item['second name']}. Enter name you want it to be changed to:")
            item['full name'] = item['first name'].capitalize() + " " + item['second name'].capitalize()
            item['city'] = input(f"Current first name is {item['city']}. Enter name you want it to be changed to:")
            return print("Updated")
    elif choice == 'c':
        return None


##############################################
#                     MAIN BODY              #
##############################################

try:
    while True:
        choice = input("""
    What are you looking for?
    (q) - quit book
    (a) - add new entry
    (s) - search 
    (d) - delete record for a given tel num
    (u) - update record for a given tel num
        """)
        if choice.strip().lower() == "q":
            print("Thank you for using #num Book")
            break
        elif choice.strip().lower() == "a":
            user_add_new()
        elif choice.strip().lower()=="s":
            print("""You can search:
            (f) - search by first name
            (s) - search by second name
            (n) - search by full name
            (t) - search by tel num
            (c) - search by city
            """)
            choice = input("Choose operation: ")
            if choice.strip().lower() == "f":
                search('first name', first_name)
            elif choice.strip().lower() == "s":
                search('second name', second_name)
            elif choice.strip().lower() == "n":
                search('full name', full_name)
            elif choice.strip().lower() == "t":
                search('phone', phone)
            elif choice.strip().lower() == "c":
                search("city",city)
            else:
                print("Not available operation")
        elif choice.strip().lower() == "d":
            phone = input("Please, enter phone number: ") 
            delete(phone)
        elif choice.strip().lower() == "u":
            phone = input("Please, enter phone number: ") 
            update(phone)
        else:
            print("Incorrect input")
            continue
except Exception as e:
    print(f"Error occured: {e}, but data is saved." )
finally:
    with open('json_buffer',"w") as json_file:
        json.dump(phonebook,json_file,indent=4)
json_file.close()