
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

nums = [0, 1, 2, 5, 7, 3]
for num in nums:
    print(num)

lang = 'Python'
for line in lang:
    print(line)

for i in range(len(lang)):
    print(lang[i])

for num in nums:
    print(num)

student={
    'first_name': 'Findlay',
    'last_name': 'Duffy',
    'age': 18,
    'country': 'UK',
    'skills': ['Python', 'HTML'],
    'address': {
        'street': 'Ost street',
        'zipcode': '77742'
    }
}

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)

It = ['Google', 'Microsoft', 'Sony', 'Amazon', 'Apple']
for company in It:
    print(company)

numbers = (0, 7, 6, 4, 3)
for number in numbers:
    print(number)
    if number == 6:
        continue
    print('The next number is:', number + 1) if numbers != 3 else print('Loop end')
print('Outside loop')

first = list(range(15))
print(first)
Set = set(range(1, 15))
print(Set)

first = list(range(0, 15, 4))
print(first)
print(Set)

for numbers in range(15):
    print(number)
        
for key in student:
    if key == 'skills':
        for skill in student['skills']:
            print(skill)

for number in range(15):
    print(number)        
else:
    print('The loop stops:', number)

for number in range(12):
    pass

for num in range(11):
    print(num)
    print('------')

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in range(11-0):
    numbers.reverse
    print(numbers)
    print('------')

count1 = 10
while count1 != 0:
    print(count1)
    count1 = count1 - 1
    if count1 == 0:
        break
else:
    print(count1)
    
count2 = 0
for call in numbers:
    if count2 < 7:
        print('call')
        count2 = count2 + 1
        if count2 >= 7:
            print('Loop stopped.')
            break


count3 = 0
for hash in numbers:
    if count3 < 8:
        print('#\t', '#\t', '#\t', '#\t', '#\t', '#\t', '#\t', '#\t')
        count3 = count3 + 1
        if count3 >= 8:
            print('Loop over.')
            break

ans = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

a0 = '0 x 0 = {}'.format(ans[0])
a1 = '1 x 1 = {}'.format(ans[1])
a2 = '2 x 2 = {}'.format(ans[2])
a3 = '3 x 3 = {}'.format(ans[3])
a4 = '4 x 4 = {}'.format(ans[4])
a5 = '5 x 5 = {}'.format(ans[5])
a6 = '5 x 5 = {}'.format(ans[6])
a7 = '7 x 7 = {}'.format(ans[7])
a8 = '8 x 8 = {}'.format(ans[8])
a9 = '9 x 9 = {}'.format(ans[9])
a10 = '10 x 10 = {}'.format(ans[10])
print(a0 +'\n' + a1 + '\n' + a2 + '\n' + a3 + '\n' + a4 + '\n' + a5 + '\n' + a6 + '\n' + a7 + '\n' + a8 + '\n' + a9 + '\n' + a10)

count4 = 0
programming = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for i in programming:
    print(i)
