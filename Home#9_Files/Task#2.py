"""
Acceptance Criteria
1. File present, if file doesn't exists - raise an error 
2. Application works with json read and save
3. Promt user with options:
   a. Add entry
   b. Find entry:
        Search by first name 
        Search by last name 
        Search by full name
        Search by telephone number
        Search by city or state
   c. Delete entry by phonenumber
   d. Update entry by phonenumber
   e. Exit app
4. Save phone book into json file after exit
5. Read existing phonebook from json file
The first argument to the application should be the name of the phonebook.
Algorithm:
1. open file
2. raise an error if file doesn't exist
3. read json
4. if during reading error appears ignore and create empty list
5. try except finally on global level to save file anyway
6. Print menu
7. if user selected add new record:
   1. Ask user put data
   2. Append data to list
8. if user selected search/delete record:
   1. ...
"""
import json
json_file= open("json_buffer")
try:
    phonebook = json.load(json_file)
except json.decoder.JSONDecodeError:
    phonebook = []
json_file.close()
def validation_num(phone):
    if phone.isdigit():
        return phone
    print('Incorrect input. Try again')
def validation_name(name):
    if name..isalpha():
        return name
    print('Incorrect input. Try again')
dict_json = {
'first name':'',
'second name':'',
'full name':'',
'phone':'',
'city':''
}
def user_add_new():
    first_name = input("Please, enter first name: ").capitalize()
    second_name = input("Please, enter second name: ").capitalize()
    full_name = first_name.capitalize() + " " + second_name.capitalize()
    phone_num = input("Please, enter phone number: ")
    city = input("Input the city: ")
    new_add = dict_json.copy()
    new_add['first name'] = first_name.capitalize()
    new_add['second name'] = second_name.capitalize()
    new_add['full name'] = full_name
    new_add['phone'] = phone_num
    new_add['city'] = city
    phonebook.append(new_add)
def search_first():
    first_name = validation_name(input("Please, enter first name you want to find: ").capitalize())
    for item in phonebook:
        if item['first name']==first_name:
            print(item)
def search_second():
    second_name = validation_name(input("Please, enter second name you want to find: ").capitalize())
    for item in phonebook:
        if item['second name']==second_name:
            print(item)
def search_full():
    full_name = input("Please, enter full name you want to find: ").capitalize()
    for item in phonebook:
        if item['full name']==full_name:
            print(item)
def search_tel():
    phone_num = validation_num(input("Please, enter phone number you want to find user of: "))
    for item in phonebook:
        if item['phone']==phone_num:
            print(item)
def search_city():
    city = input("Please, enter full name you want to find: ").capitalize()
    for item in phonebook:
        if item['city']==city:
            print(item)
def delete(phone):
    for item in phonebook:
        if item['phone']==phone:
            phonebook.remove(item)
def update(phone):
    for item in phonebook:
        if item['phone']==phone:
            item['first name'] = input(f"Current first name is {item['first name']}. Enter name you want it to be changed to:")
            item['second name'] = input(f"Current first name is {item['second name']}. Enter name you want it to be changed to:")
            item['full name'] = item['first_name'].capitalize() + " " + item['second_name'].capitalize()
            item['city'] = input(f"Current first name is {item['city']}. Enter name you want it to be changed to:")
try:
    while True:
        choice = input("""
    What are you looking for?
    (q) - quit book
    (a) - add new entry
    (f) - search by first name
    (s) - search by second name
    (n) - search by full name
    (t) - search by tel num
    (c) - search by city or state
    (d) - delete record for a given tel num
    (u) - update record for a given tel num
        """)
        if choice.strip().lower() == "q":
            print("Thank you for using #num Book")
            break
        elif choice.strip().lower() == "a":
            user_add_new()
        elif choice.strip().lower() == "f":
            search_first()
        elif choice.strip().lower() == "s":
            search_second()
        elif choice.strip().lower() == "n":
            search_full()
        elif choice.strip().lower() == "t":
            search_tel()
        elif choice.strip().lower() == "c":
            search_city()
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
    with open("json_buffer","w") as json_file:
        json.dump(phonebook,json_file,indent=4)
