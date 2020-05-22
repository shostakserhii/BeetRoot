class Person():

    def __init__(self, name, age, sex, lessons, education, purpose):
        self.name = name
        self.age = age
        self.sex = sex
        self.education = education
        self.purpose = purpose
        self.lessons = lessons

    def __str__(self):
        return f" {self.name.capitalize()} is {self.sex} of {self.age} year old.\n Education level is {self.education}. \nIn shool cause of {self.purpose} and has {self.lessons} a day."
    def __repr__(self):
        return f" {self.name.capitalize()} is {self.sex} of {self.age} year old.\n Education level is {self.education}. \nIn shool cause of {self.purpose} and has {self.lessons} a day."

class Student(Person):

    def __init__(self, name, age, sex, lessons, grades, homeworkcize, education = 'school', purpose = 'learning'):
        super().__init__(name, age, sex, lessons, education, purpose)
        self.grades = grades
        self.homeworkcize = homeworkcize
    
    def __str__(self):
        return f"""
        {self.name.capitalize()} is {self.sex} of {self.age} year old.
        Education level is {self.education}.
        In shool cause of {self.purpose} and has {self.lessons} lessons a day.
        Marks are {self.grades}.
        Has {self.homeworkcize} homework
        """
    def __repr__(self):
        return f"""
        {self.name.capitalize()} is {self.sex} of {self.age} year old.
        Education level is {self.education}.
        In shool cause of {self.purpose} and has {self.lessons} lessons a day.
        Marks are {self.grades}
        Has {self.homeworkcize} homework
        """
class Teacher(Person):

    def __init__(self, name, age, sex, lessons, sallary, education = 'university', purpose = 'teaching'):
        super().__init__(name, age, sex, lessons, education, purpose)
        self.sallary = sallary

    def __str__(self):
        return f"""
        {self.name.capitalize()} is {self.sex} of {self.age} year old.
        Education level is {self.education}.
        In shool cause of {self.purpose} and has {self.lessons} lessons a day.
        Earn {self.sallary} per year"""

    def __repr__(self):
        return f"""
        {self.name.capitalize()} is {self.sex} of {self.age} year old.
        Education level is {self.education}.
        In shool cause of {self.purpose} and has {self.lessons} lessons a day.
        Earn {self.sallary} per year"""

teacher = Teacher('Erica', '28', 'female', '5', '70000')
print(str(teacher))
student = Student('Taras', '15', 'male', '7', 'bad', 'not much' )
print(str(student))