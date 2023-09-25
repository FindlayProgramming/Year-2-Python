import numpy as np
import math
import statistics

def first_func():
    first = 'Findlay'
    last = 'Duffy'
    space = ''
    full = first + space + last
    print(full)
first_func()

def two_num():
    first_num = 5
    second_num = 9
    total = first_num + second_num
    print(total)
two_num()

name = 'Findlay'

def func(name):
    msg = name +  ', hello'
    return msg
print(func('Findlay'))

def add(num):
    fifty = 50
    return num + fifty
print(add(95))

def area(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area(10))

def sum(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum(25))
print(sum(250))

def full_name_generation(f_name, l_name):
    space = ' '
    full = f_name + space + l_name
    return full
print('Full name:', full_name_generation('Findlay', 'Duffy'))

def object_weight(mass, gravity):
    weight = str(mass * gravity)
    return weight
print('Weight of object in Newtons:', object_weight(500, 15.5))

def even(n):
    if n % 2 == 0:
        print('even')
        return True
    return False
print(even(80))
print(even(50465474643))

def find_even(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
        return evens
print(find_even(10))

def func_default(num = 24):
    msg = name + ', Welcome'
    return msg
print(func_default())
print(func_default('Findlay'))

def func_arg(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(func_arg(7, 70, 777))

def func_generation(team, *args):
    print(team)
    for i in args:
        print(i)
print(func_generation('Team-7', 'Fin', 'Sam', 'Mark'))
    
def square_num(n):
    return n * n
def action(y, x):
    return y(x)
print(action(square_num, 5))

def add_two_num(num_one, num_two):
    total = num_one * num_two
    return total
print(add_two_num(25, 100))

def area_of_circle(r):
    PI = 3.14
    area = PI * r * r
    return area
print(area_of_circle(6))

def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(add_all_nums(50, 6, 777))

def convert_celsius_to_farenheit(F, C):
    formula = F = (C * 9/5) + 32
    return formula
print(convert_celsius_to_farenheit(10, 50))

def calculate_slope():
    X = np.linspace(0, 10, 11)
    Y = np.linspace(0, 20, 11)
    Y = np.c_[Y, Y, Y]
    X = X - X.mean()
    Y = Y - Y.mean()
    slope = (X.dot(Y)) / (X.dot(X))
calculate_slope()

def print_list(*lists):
    for i in range(0, len(lists)):
        print(lists[i])
list1 = [2, 1, 5]
print_list(*list1)

def reverse_list(array):
    for i in array:
        i = array[::-1]
        print(i)
        break
list2 = [9, 8, 7, 6, 5]
reverse_list(list2)

def capitalize_list_items(lists):
    for i in lists:
        i = i.upper()
        print(i.upper())
        print(i)
list3 = ['apple', 'sony', 'microsoft', 'meta']
capitalize_list_items(list3)

def add_item(lists, item):
    for i in lists:
        i = lists[item]
        print(i)
        break
list4 = ['Ratchet', 'Clank', 'T', 'M']
print(add_item(list4, 1))

def sum_of_numbers(num1, num2):
    sum = 0
    for i in range(num1, num2 + 1):
        sum += i
        print(sum)
sum_of_numbers(4, 5)

def sum_of_odds(num1, num2):
    for num in range(num1, num2 + 1):
        if num % 2 != 0:
            print(num)
sum_of_odds(2, 17)
        
def sum_of_even(num1, num2):
    for num in range(num1, num2 + 1):
        if num % 2 == 0:
            print(num)
sum_of_even(2, 20)

def even_and_odds(positive):
    for num in range(positive + 1):
        if num % 2 == 0:
            print('Number of evens:', str(num))
        if num % 2 != 0:
            print('Number of odds:', str(num))
even_and_odds(50)

def factorial(whole):
   factorial = 1
   if whole < 0:
       print('Factorial does not exist for negative numbers.')
   elif whole == 0:
       print('Factorial of 0 is 1')
   else:
       for i in range(1, whole + 1):
           factorial = factorial * i
       print('The factorial of', whole, ':', factorial)
factorial(5)

def is_empty(empty):
    print(bool(empty))
is_empty('HL')


def take_list(number):
    calculate_mean = np.mean(number)
    calculate_median = np.median(number)
    calculate_mode = statistics.mode(number)
    calculate_range = np.ptp(number)
    calculate_variance = np.var(number)
    calculate_standard_deviation = statistics.stdev(number)
    print('Mean:', calculate_mean)
    print('Median:', calculate_median)
    print('Mode:', calculate_mode)
    print('Range', calculate_range)
    print('Variance:', calculate_variance)
    print('Standard Deviation:', calculate_standard_deviation)
take_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def is_prime(prime):
    for i in range(2, prime):
        if (prime%i) == 0:
            return False
        return True
print(is_prime(9))

def check_items_unique(items):
    if len(set(items)) == len(items):
        print('Elements are unique.')
    else:
        print('Elements are not unique')
check_items_unique(['Green', 'Yellow', 'Blue', 'Red'])

def check_item_datatype(items):
    res = True
    for i in items:
        if not isinstance(i, type(items[0])):
            res = False
            break
    print('Elements have same type?' + str(res))
check_item_datatype(['Fin', 18, 'noureal'])

def variable_validation(variable):
        i = variable.isidentifier()
        if i is False:
            print('Not a valid variable.')
        else:
            print('Variable is valid.')
variable_validation('Variable')

