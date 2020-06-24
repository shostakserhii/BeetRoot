import json
from os import path
from typing import Optional, List, Dict, Any


class User():
    def __init__(self,
                first_name: str = '',
                second_name: str = '',
                phone: str = '',
                city: str = '',
                full_name: str = '') -> None:

        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self.city = city
        self.full_name = (self.first_name + " " + self.second_name)

    def __str__(self) -> str:
        return f"""
                First name: {self.first_name}
                Second_name: {self.second_name}
                Phone: {self.phone}
                City {self.city}
                Full name: {self.full_name}"""

    def __repr__(self) -> str:
        return f"""
                First name: {self.first_name}
                Second_name: {self.second_name}
                Phone: {self.phone}
                City {self.city}
                Full name: {self.full_name}"""

    def convert(self) -> Dict[str, str]:
        return {
            'first_name': self.first_name,
            'second_name': self.second_name,
            'phone': self.phone,
            'city': self.city,
            'full_name': self.first_name + " " + self.second_name
        }

phonebook: List[User] = []
##################################################
#           VARIABLES                            #
##################################################


first_name = 'first name'
second_name = 'second name'
full_name = 'full name'
phone = 'phone'
city = 'city'

validation_listing: List[str] = [first_name, second_name, city, full_name]

####################################################
#               Validations                        #
####################################################


def validation_num(phone: str) -> bool:
    return phone.isdigit()


def validation_name(name: str) -> bool:
    return name.isalpha()


def validation_with_optional_value_return(inputing: str, category: str) -> Optional[str]:
    if category == 'phone':
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

"""def new_user() -> None:
    try:
        first_name: str = input("Enter first name: ").capitalize()
        if validation_name(first_name) is False:
            raise ValueError("Name should be of alphabetic symbols only")
        second_name: str = input("Enter second name: ").capitalize()
        if validation_name(second_name) is False:
            raise ValueError("Name should be of alphabetic symbols only")
        phone: str = input("Enter phone: ")
        if validation_num(phone) is False:
            raise ValueError("Phone should be of numbers only")
        city: str = input("Enter city: ").capitalize()
        if validation_name(city) is False:
            raise ValueError("City should be of alphabetic symbols only")
        full_name: str = (first_name + '' + second_name)
        new_user = User(first_name, second_name, phone, city, full_name)
        phonebook.append(new_user)
        print("\n\tNew abonent was added...")

    except ValueError as er:
        print(er)"""
def new_user(first_name, second_name, phone, city, full_name) -> User:
    new_user = User(first_name, second_name, phone, city, full_name)
    return new_user

def new_user_input() -> None:
    try:
        first_name: str = input("Enter first name: ").capitalize()
        if validation_name(first_name) is False:
            raise ValueError("Name should be of alphabetic symbols only")
        second_name: str = input("Enter second name: ").capitalize()
        if validation_name(second_name) is False:
            raise ValueError("Name should be of alphabetic symbols only")
        phone: str = input("Enter phone: ")
        if validation_num(phone) is False:
            raise ValueError("Phone should be of numbers only")
        city: str = input("Enter city: ").capitalize()
        if validation_name(city) is False:
            raise ValueError("City should be of alphabetic symbols only")
        full_name: str = (first_name + '' + second_name)
        new_user(first_name, second_name, phone, city, full_name)
        phonebook.append(new_user)
        print("\n\tNew abonent was added...")
    except ValueError as er:
        print(er)


def delete(phones: str, value = phonebook) -> None:
    print(f"value in delete {value}")
    for item in value:
        if item.phone == phones:
            print(f"item {item}")
            print(f"Successfuly removed {item}")
            value.remove(item)


def update(phone: str) -> None:
    for item in phonebook:
        if item.phone == phone:
            try:
                new_first_name: str = input(f"First name is {item.first_name}. Enter name you want it to be changed to: ")
                if validation_name(new_first_name) is False:
                    raise ValueError("Name should be of alphabetic symbols only")
                
                new_second_name: str = input(f"Second name is {item.second_name}. Enter name you want it to be changed to: ")
                if validation_name(new_second_name) is False:
                    raise ValueError("Name should be of alphabetic symbols only")

                new_city: str = input(f"City is {item.city}. Enter name you want it to be changed to: ")
                if validation_name(city) is False:
                    raise ValueError("City should be of alphabetic symbols only")

                item.first_name = new_first_name.capitalize()
                item.second_name = new_second_name.capitalize()
                item.city = new_city.capitalize()
                item.full_name = item.first_name.capitalize() + " " + item.second_name.capitalize()

            except ValueError as er:
                print(er)

def what_to_do(item: User) -> None:
    choice = input("""
        What do you want to do with abonent:
                    d - delete
                    u - update
                    c - continue seraching
    """).strip().lower()
    if choice == 'd':
        phonebook.remove(item)
        print("Abonent is erased")
        return None
    elif choice == 'u':

        try:
            new_first_name = input(f"First name is {item.first_name}. Enter name you want it to be changed to: ")
            if validation_name(new_first_name) is False:
                raise ValueError("Name should be of alphabetic symbols only.")
            
            new_second_name = input(f"Second name is {item.second_name}. Enter name you want it to be changed to: ")
            if validation_name(new_second_name) is False:
                raise ValueError("Name should be of alphabetic symbols only.")

            new_city = input(f"City is {item.city}. Enter name you want it to be changed to: ")
            if validation_name(city) is False:
                raise ValueError("City should be of alphabetic symbols only.")

            new_phone = input(f"City is {item.phone}. Enter name you want it to be changed to: ")
            if validation_num(new_phone) is False:
                raise ValueError("Phone should be of numbers only.")

            item.first_name = new_first_name.capitalize()
            item.second_name = new_second_name.capitalize()
            item.city = new_city.capitalize()
            item.phone = new_phone
            item.full_name = item.first_name.capitalize() + " " + item.second_name.capitalize()
            print("Updated")

        except ValueError as er:
            print(f"{er} \n'Changes cannot be applied\n\tExitting...'")

    elif choice == 'c':
        return None


def search(operation: str, phonebook: list = phonebook) -> None:
    value = validation_with_optional_value_return(input(f"Enter {str(operation)} you want to find: "), operation)
    if value is None:
        print("wrong input")
        return None
    else:
        i = 0
        for item in phonebook:
            if getattr(item, operation) == value:
                i += 1
                print(f"\nAbonent #{i}\n")
                print(item)
                what_to_do(item)
        if i == 0:
            print("No results found")
            return None

            
##############################################
#                     MAIN BODY              #
##############################################


try:
    filename = input("Filename for database if that exists: ")
    filename = 'json_file'
    if path.exists(filename):
        json_file = open(filename)
        new_json = json.load(json_file)
        for item in new_json:
            phonebook.append(User(**item))
    else:
        raise FileNotFoundError("No file in directory. Database is created being empty")

except json.decoder.JSONDecodeError:
    phonebook = []

except FileNotFoundError:
    phonebook = []

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
            new_user_input()
        elif choice.strip().lower() == "s":
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
    with open('json_file', 'w') as json_file:
        json.dump(phonebook, json_file, indent=4)
