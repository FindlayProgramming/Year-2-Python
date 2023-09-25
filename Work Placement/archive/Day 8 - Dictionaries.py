
empty_dict = {}

dct = {'k1':'val1', 'k2':'val2', 'k3':'val3', 'k4':'val4', 'k5':'val5'}
test = {
    'first_name':'Findlay',
    'last_name':'Duffy',
    'age':18,
    'country':'UK',
    'skills':'Python',
    'address':{
        'street':'ff street',
        'zipcode':'77723'
    }
}

print(len(test))
print(test['first_name'])
dct['k6'] = 'val6'
print(dct)

test['work_placement'] = 'AST'
print(test)

dct['k1'] = 'val-one'
print(dct)

print('k3' in dct)
print('k7' in dct)

dct.pop('k1')
dct.popitem()
del dct['k3']
print(dct)

print(dct.items())

dct_copy = dct.copy()

keys = dct.keys()
print(keys)

print(dct.clear())
del dct

dog = {
    'name':'Bob',
    'color':'Brown',
    'breed':'Labrador',
    'age':10
    }

Student = {
    'first_name':'Findlay',
    'last_name': 'Duffy',
    'gender':'Male',
    'age':18,
    'skills':'Python',
    'country':'UK',
    'city':'Cleveland',
    'address':{
        'street':'io',
        'zipcode':'77742'
    }
    }

print(len(Student))

values1 = Student.values()
print(values1)
print(Student['skills'])
Student['skills'] = 'HTML', 'JavaScript', 'C#'
print(Student)

Studentkeys = Student.keys()
print(keys)

print(Student.items())
Student.pop('city')

del dog