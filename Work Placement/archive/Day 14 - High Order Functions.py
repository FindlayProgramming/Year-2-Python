from functools import reduce
from countries import countries 
from itertools import chain
#High order functions: Functions can take one or more functions as parameters. 
#A function can be returned as a result of another function.
#A function can be modified.
#A function can be assigned to a variable.

def sum_num(nums):
    return sum(nums)

def higher_order_function(i, lst):
    summation = i(lst)
    return summation
result = higher_order_function(sum_num, [5, 4, 3, 2, 1])
print(result)

def square(x):
    return x ** 8

def cube(x):
    return x ** 5

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_func(t):
    if t == 'square':
        return square
    elif t == 'cube':
        return cube
    elif t == 'absolute':
        return absolute

result = higher_order_func('square')
print(result(5))
result = higher_order_func('cube')
print(result(8))
result = higher_order_func('absolute')
print(result(-10))

#def add(): ---Example---
    #ten = 10
    #def add_1(num):
        #return num + ten
    #return add_1

#closure = add()
#print(closure(10))
#print(closure(15))

def greet():
    return 'Welcome'
def upper_deco(func):
    def wrap():
        f = func()
        make_uppercase = f.upper()
        return make_uppercase
    return wrap
i = upper_deco(greet)
print(i())

def upper_deco(func):
    def wrap():
        f = func()
        make_uppercase = f.upper()
        return make_uppercase
    return wrap
@upper_deco
def greet():
    return 'Welcome'
print(greet())

def upper_deco(func):
    def wrap():
        f = func()
        make_uppercase = f.upper()
        return make_uppercase
    return wrap

def split_string_deco(func):
    def wrap():
        f = func()
        split_str = f.split()
        return split_str
    return wrap

@split_string_deco
@upper_deco
def greet():
    return 'Welcome'
print(greet())

def deco_with_parameters(func):
    def wrapper_accepting_parameters(para1, para2, para3):
        func(para1, para2, para3)
        print('Lives in: {}'.format(para3))
    return wrapper_accepting_parameters

@deco_with_parameters
def print_full_name(first_name, last_name, country):
    print('I am {} {}. I love to learn.'.format(
        first_name, last_name, country))

print_full_name('Findlay', 'Duffy', 'UK')

num = [5, 4, 3, 2, 1]
def square(x):
    return x ** 8
num_squared = map(square, num)
print(list(num_squared))
num_squared = map(lambda x : x ** 5, num)
print(list(num_squared))

num_str = ['5', '4', '3', '2', '1']
num_int = map(int, num_str)
print(list(num_int))

name = ['Findlay', 'Sam', 'Steven', 'Dan']

def change_to_upper(names):
    return names.upper()

name_upper_cased = map(change_to_upper, name)
print(list(name_upper_cased))

name_upper_cased = map(lambda names: names.upper(), name)
print(list(name_upper_cased))

nums = [5, 4, 3, 2, 1]
def is_even(num):
    if num % 2 == 0:
        return True
    return False
even_numbers = filter(is_even, nums)
print(list(even_numbers))

name1 = ['Findlay', 'Sam', 'Steven', 'Dan']

def is_name_long(names):
    if len(names) > 7:
        return True
    return False

long_names = filter(is_name_long, name1)
print(list(long_names))

num_str = ['1', '2', '3', '4', '5']
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, num_str)
print(total)

#Level 1 Map: The map function is a built-in function that takes a function and iterable as parameters.
#Level 1 Filter: The filter function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.
#Level 1 Reduce: The reduce function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable.

#Level 1  Q2 Higher order function: 1.Functions are treated with importance, allowing the user to perform numerous operations on functions such as taking in one or more functions as parameters, 2.functions can be returned as a result of another function. 3.Functions can be modified. 4.Functions can be assigned to a variable.
#Level 1 Q2 Closure: Python allows a nested function to access the outer scope of the enclosing function and is referred to as a closure. In python, closures are created through nesting a function inside another encapsulating funtion and then returning the inner function.
#Level 1 Q2 Decorator: A decorator is a design pattern in python that allows users to add new functionality to an existing object without modifying its structure. Creating decoraters requires an inner wrapper function.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9] #Level 1 Q3.
def times(x):
    return x * 25
numbers_multiplied = map(times, num)
print(list(numbers_multiplied))
numbers_multiplied = map(lambda x : x * 50, num)
print(list(numbers_multiplied))

def odd(number):
    if number % 2 != 0:
        return True
    return False

odd_num = filter(odd, num)
print(list(odd_num))

string_lst = ['10', '5', '4', '6', '7', '2']
def num(x, y):
    return int(x) + int(y)

total = reduce(num, string_lst)
print(total)

for i in countries: #Level 1 Q4.
    print(i)

names = ['Fin', 'Dan', 'Kai', 'Steven', 'Chris', 'Mark', 'Patrick', 'John', 'Jake', 'Jack', 'Liam'] #Level 1 Q5.
for i in names:
    print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50, 100, 400, 500, 700, 900, 1500, 2000] #Level 1 Q6.
for i in numbers:
    print(i)

def country_upper(country): #Level 2 Q1.
   return country.upper()
countries_upper_cased = map(country_upper, countries)
print(list(countries_upper_cased))

countries_upper_cased = map(lambda country: country.upper(), countries)
print(list(countries_upper_cased))

nums = [5, 6, 7, 8, 9, 4, 3, 2, 1] #Level 2 Q2.
def num_to_square(x):
    return x ** 2
num_squared = map(num_to_square, nums)
print(list(num_squared))
num_squared = map(lambda x : x ** 2, nums)

def change_names_to_upper(name): #Level 2 Q3.
    return name.upper()
names_upper = map(change_names_to_upper, names)
print(list(names_upper))

def filter_out(country): #Level 2 Q4.
    if 'land' in country:
        return True
    return False
filter_country = filter(filter_out, countries)
print(list(filter_country))

def filter_6_chars(country): #Level 2 Q5.
    if len(country) == 6:
        return True
    return False
filter_chars = filter(filter_6_chars, countries)
print(list(filter_chars))

def filter_6or_more_chars(country): #Level 2 Q6.
    if len(country) >= 6:
        return True
    return False
filter_charss = filter(filter_6or_more_chars, countries)
print(list(filter_charss))

def filter_out(country): #Level 2 Q7.
    if 'E' in country[0]:
        return True
    return False
filter_country = filter(filter_out, countries)
print(list(filter_country))

odd_1 = [1, 5, 9, 7, 3] #Level 2 Q8.
even = [2, 4, 8, 6]

def chain(*iterables):
    for i in iterables:
        for each in i:
            yield each

numbers = list(chain(odd_1, even))
print(numbers)

def get_string_lists(lst):
    for i in lst:
      sum = '\n'.join(map(str, lst))
      return sum
print(get_string_lists(names))

def reduce_to_sum(num1, num2):
    return int(num1) + int(num2)
numbers_sum = reduce(reduce_to_sum, numbers)
print(numbers_sum)

country1 = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'and', 'Iceland' , 'are all north European countries.']
def reduce_concatenate_lst(lst):
    for i in lst:
        concatenated_str = ','.join(map(str, lst))
        return concatenated_str
print(reduce_concatenate_lst(countries))
    