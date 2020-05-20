class Person():

    def __init__(self, name, age, sex, education = school, lessons, purpose = learning):
        self.name = name
        self.age = age
        self.sex = sex
        self.education = education
        self.lessons = lessons
        self.purpose = purpose
    
    def __str__(self):
        return f" {self.name.capitalize()} is {self.sex} of {self.age} year old.\n Education level is {self.education}. \nIn shool cause of {self.purpose} and has{lessons} a day."
    def __repr__(self):
        return f" {self.name.capitalize()} is {self.sex} of {self.age} year old.\n Education level is {self.education}. \nIn shool cause of {self.purpose} and has{lessons} a day."
class Student(Person):

    def grades(grades = good):
        self.grades = grades
    
    def homework(self):
        self.homework = homework
    
class Teacher(Person):

    def sallary(self):
        self.sallary = sallary

teacher = Teacher(self, name = 'Erica', age = 28, sex = 'female', education = 'university', lessons = 5, purpose = 'teaching')
print(str(teacher))
