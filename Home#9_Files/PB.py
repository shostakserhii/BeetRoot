import json
phonebook = []
class User():

    def __init__(self,first_name = None,second_name = None,phone = None,city = None, full_name = None):
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self.city = city
        self.full_name = self.first_name+" "+self.second_name

#    def __str__(self):
#        return print(f'first name: {self.first_name} second_name: {self.second_name} phone: {self.phone} city {self.city} fullname: {self.full_name}')
#
#    def __repr__(self):
#       return print(f'first name: {self.first_name} second_name: {self.second_name} phone: {self.phone} city {self.city} fullname: {self.full_name}')

    def convert(self):
        return {
            'first_name':self.first_name,
            'second_name':self.second_name,
            'phone':self.phone,
            'city':self.city,
            'full_name':self.first_name+" "+self.second_name
        }
####################################################
#               BODY FUNCTIONS                     #
####################################################

def new_user():
    first_name = input("Enter first name: ")
    second_name = input("Enter second name: ")
    phone = input("Enter phone: ")
    city = input("Enter city: ")
    full_name = (first_name + "" + second_name)
    new_user = User(first_name, second_name, phone, city , full_name)
    phonebook.append(new_user)


def delete(phone):
    for item in phonebook:
        if item.phone==phone:
            phonebook.remove(item)
            print(f"Successfuly removed {item}")


def update(phone):
    for item in phonebook:
        if item.phone==phone:
            item.first_name = input(f"First name is {item.first_name}. Enter name you want it to be changed to: ")
            item.second_name = input(f"Second name is {item.second_name}. Enter name you want it to be changed to: ")
            item.full_name = item.first_name.capitalize() + " " + item.second_name.capitalize()
            item.city = input(f"City is {item.city}. Enter name you want it to be changed to: ")


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
            item.first_name = input(f"First name is {item.first_name}. Enter new first name: ")
            item.second_name = input(f"Second name is {item.second_name}. Enter new second name: ")
            item.full_name = item.first_name.capitalize() + " " + item.second_name.capitalize()
            item.city = input(f"City is {item.city}. Enter new city: ")
            item.phone = input(f"Phone is: {item.phone}. Enter new phone: ")
            return print("Updated")
    elif choice == 'c':
        return None

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
                search_first()
            elif choice.strip().lower() == "s":
                search_second()
            elif choice.strip().lower() == "n":
                search_full()
            elif choice.strip().lower() == "t":
                search_tel()
            elif choice.strip().lower() == "c":
                search_city()
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
except ValueError as e:
    print(f"Error: {e} happened but data is saved, all ok! ")
finally:
    phonebook = [new_user.convert() for new_user in phonebook]
    with open('json_file','w') as json_file:
        json.dump(phonebook, json_file, indent = 4)
