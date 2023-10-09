F1 = ['Ferrari', 'Williams', 'Haas', 'Racing Point']

print(F1)
print('Bonus:', F1[0])

Team2 = ['Myers', 'V', 'Jackie', 'Tony', 'Hasan']

print(Team2, 'are their rivals!')

F1[3] = 'Aston Martin'

Team3 = ['Joe', 'Chris', 'Jonathan', 'Liam', 'Kyle']

F1.append(Team2)
F1.append(Team3)
print(F1)
'''
replace = int(input('Which user would you like to replace 0-5?'))
new_team = input('What will be the name of the new team?')
F1[replace] = new_team
print(F1)
'''

drivers = ['John', 'Dave', 'Bob', 'Kyle']
wages = [20, 14, 7, 5]

print(drivers[0], wages[0])
print(drivers[1], wages[1])
print(drivers[2], wages[2])
print(drivers[3], wages[3])

for total_wage in wages:
    print(total_wage)
    total_wage = +1

#Tuple - slicing/indexing
tpl = ('Fin', 4, 3.55)
tpl[0:2]
tpl[-1]