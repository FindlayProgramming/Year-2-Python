
a = 3
if a > 0:
    print('A is a negative number')
else:
    print('A is a positive number')    

aa = 0
if aa > 0:
    print('A is a positive number')
elif aa < 0:
    print('A is a negative number')
else:
    print('A is zero')
    
aaa = 3
print('A is a positive') if a > 0 else print('A is negative')

b = 0
if b > 0:
    if b % 2 == 0:
        print('B is a positive and even integer')
    else:
        print('B is a positive number')
elif b == 0:
    print('B is zero')
else:
    print('B is a negative number')
    
bb = 0
if bb > 0 and bb % 2 == 0:
    print('B is even and positive integer')
elif bb > 0 and a % 2 != 0:
    print('B is a positive integer')
elif bb == 0:
    print('B is zero')
else:
    print('B is negative')

user = 'Findlay'
access = 4
if user == 'admin' or access >= 4:
    print('Access granted.')
else:
    print('Access denied.')
    

User_input = int(input('Input your age: '))
if User_input >= 18:
    print('You are old enough to drive.')
else:
    print('You are not old enough to drive.')

my_age = 18
your_age = int(input('Enter your age: '))
age_difference = your_age - my_age
if your_age > 18:
    print('You are', age_difference, 'years older than me.')
elif your_age == my_age:
    print('We are both the same age: ', my_age)
else:
    print('Your are younger than me by', age_difference, 'years.')

num_one = int(input('Input the first number: '))
num_two = int(input('Enter the second number: '))
if num_one > num_two:
    print('number one is greater than number two.')
elif num_one < num_two:
    print('number one is smaller than number two.')
else:
    print('both numbers are equal.')
    
Grade_A = 80-100
Grade_B = 70-89
Grade_C = 60-69
Grade_D = 50-59
fF = 0-49

Grade_input = int(input('Enter your score: '))
if Grade_input == Grade_A:
    print('You have got a grade A.')
elif Grade_input == Grade_B:
    print('You have gotten a grade B.')
elif Grade_input == Grade_C:
    print('You have gotten a grade C.')
elif Grade_input == Grade_D:
    print('You have gotten a grade D.')
elif Grade_input == fF:
    print('You have failed.')
    
Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']
    
fruits1 = ['banana', 'orange', 'mango', 'lemon']
fruits1.append('apple')
fruits1.append('pineapple')
print(fruits1)

person={
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

sk = 'skills' in person
print(sk)
print(person['skills'][0])
pk = 'Python' in person
print(pk)

