import json



json_data = [{
"phone number":"0969771671",
"first name":"Serhii",
"second name":"Shostak",
"full name" :"Shostak Serhii",
"city":"rivne"
},
{
"phone number":"0968396961",
"first name":"Ivanna",
"second name":"Ver",
"full name" :"Ivana Ver",
"city":"rivne" 
}
]
phone_book = open('phone_book','w')
print(json.dump(json_data, phone_book))
phone_book.close()
def add_new():
    info = input("""
    Enter in format:  phone number : 029423423 | first name : Oleksandr | second name : Sasha| full name : Oleksandr Sasha | city : rivne
    """)
    if str_to_dict(info) not in phone_book:
        phone_book.append(info)
        phone_book.close()
    return print("Already exists")
def str_to_dict(info):
    check = info.split('|')
    parameters = [i.split(":") for i in check]
    parameters_new = {}
    for key, value in parameters:
        parameters_new[key.strip()]=value.strip()
    return parameters_new
def menu_loop():
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
        if choice == "q":
            "Thank you for using #num Book"
            break
        elif choice == "a":
            add_new()
        elif choice == "f":
            search_first()
        elif choice == "s":
            search_second()
        elif choice == "n":
            search_full()
        elif choice == "t":
            search_tel()
        elif choice == "c":
            search_city()
        elif choice == "d":
            delete()
        elif choice == "u":
            update()
        else:
            print("Incorrect input")
            continue
menu_loop()