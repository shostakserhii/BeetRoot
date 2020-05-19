import json
phonebook = []
class User():

    def __init__(self,first_name = None,second_name = None,phone = None,city = None, full_name = None):
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self.city = city
        self.full_name = self.first_name+" "+self.second_name


    def __str__(self):
        return f"""
                First name: {self.first_name} 
                Second_name: {self.second_name} 
                Phone: {self.phone}
                City {self.city} 
                Full name: {self.full_name}"""


    def __repr__(self):
        return f"""
                First name: {self.first_name} 
                Second_name: {self.second_name} 
                Phone: {self.phone}
                City {self.city} 
                Full name: {self.full_name}"""


    def convert(self):
        return {
            'first_name':self.first_name,
            'second_name':self.second_name,
            'phone':self.phone,
            'city':self.city,
            'full_name':self.first_name+" "+self.second_name
        }
    
##################################################
#           VARIABLES                            #
##################################################

first_name = 'first name'
second_name = 'second name'
full_name = 'full name'
phone = 'phone'
city= 'city'

validation_listing = [first_name, second_name, city, full_name]

####################################################
#               Validations                        #
####################################################

def validation_num(phone):
    if phone.isdigit():
        return phone
    print('Incorrect input. Try again')


def validation_name(name):
    if name.isalpha():
        return name
    print('Incorrect input. Try again')


def validation(inputing, category):
    if str(category) == 'phone':
        if inputing.isdigit():
            return inputing
        return None
    elif category in validation_listing: 
        if inputing.isalpha():
            return inputing
    print('Incorrect input. Try again')
    return None


####################################################
#               BODY FUNCTIONS                     #
####################################################

def new_user():
    first_name = input("Enter first name: ").capitalize()
    second_name = input("Enter second name: ").capitalize()
    phone = input("Enter phone: ")
    city = input("Enter city: ").capitalize()
    full_name = (first_name + '' + second_name)
    new_user = User(first_name, second_name, phone, city , full_name)
    phonebook.append(new_user)


def delete(phone):
    for item in phonebook:
        if item.phone==phone:
            print(f"Successfuly removed {item}")
            del item
            


def update(phone):
    for item in phonebook:
        if item.phone==phone:
            item.first_name = input(f"First name is {item.first_name}. Enter name you want it to be changed to: ").capitalize()
            item.second_name = input(f"Second name is {item.second_name}. Enter name you want it to be changed to: ").capitalize()
            item.full_name = item.first_name.capitalize() + " " + item.second_name.capitalize()
            item.city = input(f"City is {item.city}. Enter name you want it to be changed to: ").capitalize()


def what_to_do(item):
    choice = input("""
        What do you want to do with abonent:
                    d - delete
                    u - update
                    c - continue seraching
    """).strip().lower()
    if choice == 'd':
        phonebook.remove(item)
        return print("Abonent is erased")
    elif choice == 'u':
            item.first_name = input(f"First name is {item.first_name}. Enter new first name: ").capitalize()
            item.second_name = input(f"Second name is {item.second_name}. Enter new second name: ").capitalize()
            item.full_name = item.first_name.capitalize() + " " + item.second_name.capitalize()
            item.city = input(f"City is {item.city}. Enter new city: ").capitalize()
            item.phone = input(f"Phone is: {item.phone}. Enter new phone: ")
            return print("Updated")
    elif choice == 'c':
        return None


def search(operation):
    value = validation(input(f"Enter {str(operation)} you want to find: "),operation)
    if value is None:
        return print("wrong input") 
    else:
        i = 0
        for item in phonebook:
            if getattr(item, operation) == value:
                i+=1
                print(f"\nAbonent #{i}\n")
                print(item)
                what_to_do(item)
        if i == 0:
            return print("No results found")
##############################################
#                     MAIN BODY              #
##############################################

try:
    json_file = open('json_file')
    new_json = json.load(json_file)
    for item in new_json :
        phonebook.append(User(**item))
except json.decoder.JSONDecodeError:
    phonebook=[]
json_file.close()


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
            print("Thank you for using #NumBook")
            break
        elif choice.strip().lower() == "a":
            new_user()
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
                search('first name')
            elif choice.strip().lower() == "s":
                search('second name')
            elif choice.strip().lower() == "n":
                search('full name')
            elif choice.strip().lower() == "t":
                search(phone)
            elif choice.strip().lower() == "c":
                search("city")
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
    print(f"Error: {e} happened but data is saved, all ok! ")
finally:
    phonebook = [new_user.convert() for new_user in phonebook]
    with open('json_file','w') as json_file:
        json.dump(phonebook, json_file, indent = 4)
