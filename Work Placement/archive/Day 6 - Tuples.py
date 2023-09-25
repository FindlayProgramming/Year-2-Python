
first_tuple = tuple()
tpl = ('1', '2', '3')
print(len(tpl))
first = tpl[0]
print(first)
second = tpl[1]
print(second)
last = len(tpl) - 1
last_tpl = tpl[last]
print(last_tpl)
negative_index1 = tpl[-2]
negative_index2 = tpl[-1]
print(negative_index1,'\n'+ negative_index2)
all_tpl = tpl[0:4]
all_tpl1 = tpl[0:]
middle_two_tpl_items = tpl[0:2]
print(all_tpl,'\n', all_tpl1,'\n', middle_two_tpl_items)

all_items_negative = tpl[-2:-1]
middle_negative = tpl[-1]
print(all_items_negative,'\n' + middle_negative)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'test'
fruits = tuple(fruits)
print(fruits)

print('orange' in fruits)
print('apple' in fruits)

tpl1 = ('1', '2', '3', '4', '5')
tpl2 = ('6', '7', '8', '9', '10')
tpl3 = tpl1 + tpl2
print(tpl3)

del tpl1
del tpl2

empty_tpl = ()
brothers = ('Liam', 'Daniel', 'Flynn')
sisters = ('Fiora', 'Nidalee', 'Kiara')
siblings = brothers + sisters
print(siblings)
print('I have:', len(siblings))
parents = ('Mark', 'Christina')
family_members = siblings + parents
print(family_members)

first_member, second_member, third_member, fourth_member, fifth_member, sixth_member, *rest = family_members
print(first_member, '\n' + second_member, '\n' + third_member, '\n' + fourth_member, '\n' + fifth_member, '\n' + sixth_member, '\n', rest)

fruits = ('apple', 'banana', 'orange', 'grapes')
vegetables = ('carrot', 'sprouts', 'broccoli')
animal_products = ('dog food', 'cat food', 'cat tray', 'litter')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = (food_stuff_tp)
food_stuff_firstthree = food_stuff_lt[0:3]
print(len(food_stuff_lt))
food_stuff_lastthree = food_stuff_lt[8:11]
print(food_stuff_firstthree, '\n', food_stuff_lastthree)

del(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
