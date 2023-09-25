import itertools

lang = 'Python'
lst = list(lang)
print(type(lst))
print(lst)

last = [i for i in lang]
print(type(lst))
print(lst)

numbers = [i for i in range(11)]
print(numbers)

number = [(i , i * i) for i in range(11)]
print(number)

even = [i for i in range(21) if i % 2 == 0]
print(even)
odd = [i for i in range(21) if i % 2 != 0]
print(odd)

positive_even = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even)

list_of_lists = [[1, 2, 3], [7, 7, 7], [9, 8, 4]]
flat_list = [number for row in list_of_lists for numbers in row]
print(flat_list)

def two_nums(a, b):
    return a + b

print(two_nums(9, 8))
two_nums = lambda a, b: a + b
print(two_nums(4, 5))

(lambda a, b: a + b)(3,6)

square = lambda x : x ** 2
print(square(7))
cube = lambda x : x ** 3
print(cube(9))

multiple = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple(7, 4, 2))

def pwr(i):
    return lambda n : i ** n
cube = pwr(5)(7)
print(cube)
two_pwr = pwr(5)(5)
print(two_pwr)

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [i for i in range(7) if i % 2 == 0 and i > 0]
print(filtered)

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_lst = [number for row in lists for number in row]
print(flattened_lst)

lst_tuple = [(i, i * i) for i in range(100000)]
print(lst_tuple)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_country_list = [i for row in countries for i in row]
print(flattened_country_list)

def convert(lst):
    res_dct = map(lambda i: (lst[i], lst[i+1]), range(len(lst)-1)[::2])
    return dict(res_dct)
print(convert(flattened_country_list))

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated = names[0] + names[1] + names[2] + names[3]
print(concatenated)

for i in names:
    names.append(i)
    print(names)
    break
    
def data(x_values, y_values):
    mean = lambda i: sum(i)/len(i)
    multiply = lambda i1, i2: [a*b for a, b in zip(i1, i2)]
    
    m = ( (mean(x_values)*mean(y_values) - mean(multiply(x_values, y_values))) /
         (mean(x_values)**2)             - mean(multiply(x_values, x_values))) 
    
    b = mean(y_values) - m*mean(x_values)
    return m, b
x = [1, 2, 3, 4, 5]
y = [15, 20, 40, 50, 60]
m, b = data(x, y)
print(f'regression line: y = {round(m,2)}x + {round(b,2)}')
data(x, y)