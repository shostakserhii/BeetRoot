class Dog():
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return Dog.age_factor*self.dog_age

x = Dog(2)
print(x.human_age())
