import statistics as st

#Python is object oriented, meaning everything in Python is an object with its properties and methods.
#Every element in Python is an object of a class as it serves as a sort of blueprint for objects.
#Every class uses a function called __init__() which is used to assign values to object properties or other operations that are necessary to do when the object is being created.
#Benefits of OOP include building programs from standard working modules that communicate with one another.
#2. OOP allows the language to break the program into bit-sized problems that can be solved easily.

ids = input('Enter ID: \n')

class Person:
    def __init__ (self,name): #self allows to attach parameters to the class.
        self.name = name
p = Person('Findlay')
print(p.name)
print(p)

class student_data:
    def __init__(self, firstname, lastname, age, country, city, *args):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []
    
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} and lives in the {self.country}, {self.city}.'
    def add_skill(self, skill):
        self.skills.append(skill)

f = student_data('Findlay', 'Duffy', '18', 'UK', 'Billingham', ids)
print(f.firstname)
print(f.lastname)
print(f.age)
print(f.country)
print(f.city)
f.add_skill('HTML')

class Test(student_data):
    pass
t1 = Test('Fin', 'Du', 18, 'Finland', 'Helsinki')
print(t1.person_info())
t1.add_skill('Marketing')
print(t1.skills)

'''
class Vehicles():
    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f."

class student():
    pass
print(student)
'''

class student:
    def ID():
        idss = input('Enter ID: \n')
        print(idss)

