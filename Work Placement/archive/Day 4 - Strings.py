

first = 'Findlay'
last = 'Duffy'
print(first, last)
print(len(first) != len(last))

print('Python challenge. \nV')
print('Days\tTopics\tExercises')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('Backlash symbol (\\)')
print('Every programming language starts with \'Hello, World!\'')

lan = 'Python'
formatted_STR = 'I am {} {}. I teach {}' .format(first, last, lan)
print(formatted_STR)

radius = 5
pi = 3.14
area = pi * radius ** 2
formated_str = 'The area of circle with a radius {} is {:.2f}.' .format(radius, area)
print(formated_str)
python_libraries = ['NumPy', 'Tabulate', 'Matplotlib', 'Pandas', 'Seaborn']
formatted = 'The following are python libraries: {}.'  .format(python_libraries)
print(formatted)

a = 5
b = 7

print(f'{a} / {b} = {a / b:.2f}')

language = 'Python'
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)

greeting = 'Hello, World!'
print(greeting[::-1])

pto = language[0:6:2]
print(pto)

challenge = 'thirty days of python'
print(challenge.count ('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))

print(challenge.endswith('on'))
print(challenge.endswith('tion'))

print(challenge.find('y'))
print(challenge.find('th'))

print(challenge.rfind('y'))
print(challenge.rfind('th'))

num = '10.5'
print(num.isnumeric())

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ''.join(web_tech)
print(result)


li = ['Thirty', 'Days', 'Of', 'Python']

re = ''.join(li)
print(re)

coding = ['Coding', 'For', 'Everyone']
s = ''.join(coding)
e = 'Coding For All'
of = 'coding'
print(s.find(of))
print(s.replace('Coding', 'Python'))
print(e.split())

company = 'a'
coding.append(company)
print(company)
j = len(company)
print(j)
print(company.upper())
print(company.lower())
js = 'FSDFDFREERYNFGSDF'
print(e.capitalize())
print(e.title())
print(e.swapcase())
nl = coding[1:14]
print(nl)

Companies = 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'
o = ''.join(Companies)
print(o.split(', '))
print(e[0])
print(e[13])
print(e[10])
print(e[0], e[7], e[11])

sub_str = 'F'
print(e.index(sub_str))
sub_s = 'l'
print(e.rindex(sub_s))

sentence = 'You cannot end a sentence with because because because is a conjunction.'
print(sentence.rindex('because'))

days30 = '30DaysOfPython'
thirty = 'thirty_days_of_python'

print(days30.isidentifier())
print(thirty.isidentifier())

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

pytho = ','.join(python_libraries)
print(pytho)

new_sent = 'I am enjoying this challenge. \nI just wonder what is next.'
print(new_sent)

h = 'Name\tAge\tCountry\tCity\nAsabeneh 250 Finland Helsinki'
print(h)

radius = 10
ar = 3.14 * radius ** 2
format_str = 'The area of a circle with radius {} is {} meters square.'.format(radius, ar)
print(format_str)

t = 8
r = 6
ans = [14, 2, 48, 1.33, 2, 1, 262144]

tr = '{} + {} = {}'.format(t, r, ans[0])
rt = '{} - {} = {}'.format(t, r, ans[1])
trt = '{} * {} = {}'.format(t, r, ans[2])
rtr = '{} / {} = {}'.format(t, r, ans[3])
ttt = '{} % {} = {}'.format(t, r, ans[4])
trrt = '{} // {} = {}'.format(t, r, ans[5])
rrr = '{} ** {} = {}'.format(t, r, ans[6])

print(tr, '\n', rt, '\n', trt, '\n', rtr, '\n', ttt, '\n', trrt, '\n', rrr)