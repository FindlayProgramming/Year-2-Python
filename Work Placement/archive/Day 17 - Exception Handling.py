

#Exception Handling

try:
    name = input('Name: ')
    year = int(input('Year you were born: '))
    age = 18 - year
    print(f'I am {name}. And my age is {age}.')
except Exception as ex:
    print(ex)

#List

def sum_of_list(a, b, c, d, e):
    return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
print(sum_of_list(*lst))


nums = range(4, 8)
print(list(nums))
args = 4, 8
nums = range(*args)
print(nums)

#Tuple

companies = ['Apple', 'Meta', 'Microsoft', 'Sony', 'EVGA', 'ASUS']
ap, me, mi, *rest = companies
print(ap, me, mi, rest)
num_lst = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = num_lst
print(one, middle, last)

#Dictionary

def unpacking_dictionary(name, age, programminglanguage, hobby):
    return f'{name} is {age} years old and loves {programminglanguage} as well as {hobby}.'
dct = {'name':'Findlay', 'age':18, 'programminglanguage':'Coding/Making Algorithms', 'hobby':'Gaming'}
print(unpacking_dictionary(**dct))

def sum(*args):
    count = 0
    for i in args:
        count += i
    return count
print(sum(4, 5, 7))
print(sum(10, 9, 5, 7, 3, 4))

def info(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs

print(info(name='Findlay',
           age=18, country='UK'))

lst_one = [1, 2, 3]
lst_two = [7, 5, 4, 3]
lst = [0, *lst_one, *lst_two]
print(lst)
company_lst_one = ['MSI', 'Logitech', 'Corsair']
company_lst_two = ['Asus', 'PNY']
full_company_lst = [*company_lst_one, *company_lst_two]
print(full_company_lst)

#Enumerate

for index, item in enumerate([60, 80, 100]):
    print(index, item)
    
for index, i in enumerate(full_company_lst):
    print('Hardware')
    if i == 'MSI':
        print(f'The company {i} has been found at index {index}')

#Zip

instruments = ['Guitar', 'Drums', 'Violin', 'Piano', 'Saxophone']
not_instruments = ['U', 'G' ,'M', 'V', '1']
instruments_and_none = []
for i, v in zip(instruments, not_instruments):
    instruments_and_none.append({'instrument':i, 'none':v})
print(instruments_and_none)

full_lst = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
*rest, es, ru = full_lst
nordic_countries = [rest]
Estonia = es
Russia = ru
print('Nordic:', nordic_countries, 'Es:', Estonia, 'Ru:', Russia)

