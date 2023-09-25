import os
from Modules import generate_name as full_name, sum as total, person as p, gravity as g
import sys
from statistics import *
from math import pi as PI
import string
from random import random, randint
import random
import numpy as np

print(full_name('Findlay', 'Duffy'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

#print('Welcome {}. Enjoy {} Challenge'.format(sys.argv[1], sys.argv[2]))

ages = [18, 20, 4, 22, 26, 23, 10]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

#print(math.pi)
#print(math.sqrt(2))
#print(math.pow(2,3))
#print(math.floor(9.81))
#print(math.ceil(9.81))
#print(math.log10(100))

print(PI)

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
ii = 7

letters = string.ascii_lowercase #1.
res = ''.join(random.choices(string.ascii_letters + string.digits, k = ii))
#result = ''.join(random.choice(string.ascii_letters) for i in range)
print(str(res))

def id_gen_by_user(): #2.
    number_of_characters = int(input('number of characters:'))
    number_of_IDs = int(input('number of IDs:'))
    char = ''.join(random.choices(string.ascii_letters + string.digits, k = number_of_characters))
    num_of_id = ''.join(random.choices(string.ascii_letters + string.digits, k = number_of_IDs))
    print(char)
    print(num_of_id)
id_gen_by_user()

def rgb_color_gen(): #3.
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    rgb = [red, green, blue]
    print(rgb)
rgb_color_gen()

#def list_of_hexa_colors():
    #arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #letters = ['f', 'c', 'b', 'e', 'd', 'a']
    #hexa = arr + letters
    #random_letters = random.choices(arr)
    #print('#' + random_letters)
#list_of_hexa_colors()

def list_of_rgb_colors(): #Level 2: 2.
    rgb_array = ['Red', 'Green', 'Blue']
    rand = random.choice(rgb_array)
    print(rand)
list_of_rgb_colors()

def generate_colors(): #Level 2: 3.
    colors = int(input('How many colors?:'))
    color1 = randint(0, 255)
    color2 = randint(0, 255)
    color3 = randint(0, 255)
    if colors == 1:
        print('rgb', color1)
    elif colors == 2:
        print('rgb', color1, color2)
    else:
        print('rgb', color1, color2, color3)
generate_colors()

def shuffle_list(List): #Level 3: 1.
    random.shuffle(List)
    print(List)
print(shuffle_list([1, 4, 5, 6, 7]))

def return_array_in_a_range(): #Level 3: 2.
    arr = np.random.randint(0, 9, 7)
    print(arr)
return_array_in_a_range()