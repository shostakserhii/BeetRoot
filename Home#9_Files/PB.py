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
#        return print(f'first name: {self.first_name} second_name: {self.second_name} phone: {self.phone} city {self.city} fullname: {self.full_name}')
#
    def convert(self):
        return {
            'first_name':self.first_name,
            'second_name':self.second_name,
            'phone':self.phone,
            'city':self.city,
            'full_name':self.first_name+" "+self.second_name
        }


def new_user():
    first_name = input("Enter first name: ")
    second_name = input("Enter second name: ")
    phone = input("Enter phone: ")
    city = input("Enter city: ")
    full_name = (first_name + "" + second_name)
    new_user = User(first_name, second_name, phone, city , full_name)
    return new_user

try:
    json_file = open('json_file')
    new_json = json.load(json_file)
    for item in new_json :
        phonebook.append(User(**item))
except json.decoder.JSONDecodeError:
    phonebook=[]
json_file.close()

try:
    phonebook.append(new_user())
    phonebook = [new_user.convert() for new_user in phonebook]
except Exception as e:
    print(f"Error: {e} happened but data is saved, all ok! ")
finally:
    print(phonebook)
    with open('json_file','w') as json_file:
        json.dump(phonebook, json_file, indent = 4)
