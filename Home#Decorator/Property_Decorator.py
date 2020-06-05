class Admin_User():

    def __init__(self, password = 'q'):
        self.password = password

    @property
    def password(self):
        print("getting....")
        return self.__password

    @property
    def password(self, password):
        old = input("old password: ")
        if old == self.password:
            self.__password = password
        else: raise ValueError("wrong pass")


user = Admin_User('s')
print(user.password)