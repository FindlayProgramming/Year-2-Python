from datetime import datetime
import time
from tabulate import tabulate

m = "k"
type(m)
print(type(m))

Fin = "Findlay"
Du = "Duffy"
fi = len(Fin)
d = len(Du)
print(len(Fin))
print(len(Du))
print('The difference in my first and last name is:', fi - d, 'Characters')

num_one = 5

num_two = 4

sum = num_one + num_two
print(sum)
sub = num_one - num_two
print(sub)
div = num_one / num_two
print(div)
mul = num_one * num_two
print(mul)
mod = num_one % num_two
print('Remainder:', mod)

f = 'python'
s = 'dragon'

l = 'on' not in f
print(l)
ll = 'on' not in s
print(ll)

ss = 'I hope this course is not full of jargon'

ff = 'jargon'

fs = ff in ss

print(fs)

p = len('python')
d = float(p)
print(d)
o = str(p)
print(o)

i = int(input('Input a number: '))

if (i % 2) == 0:
    print("The number is even")
else:
    print("The number is odd")
    
ii = 7//3
jl = 2.7
ds = int(2.7)
av = ii is ds
print(av)

kl = '10'
io = 10
wq = kl is io
print(wq)

mn = int(9.8)
hj = mn == io
print(hj)

person = int(input('Enter hours: '))
rate = int(input('Enter rate per hour: '))
wk = person * rate
print('Your weekly earning is: ', wk)

years = int(input('Enter number of years you have lived: '))
sec = years*31536000
print('You have lived for: ', sec, 'seconds.')

table = [['Table'],
         [1, 1, 1, 1, 1],
         [2, 1, 2, 4, 8],
         [3, 1, 3, 9, 27],
         [4, 1, 4, 16, 64],
         [5, 1, 5, 25, 125]]

table1 = tabulate(table)
table2 = tabulate(table, headers='firstrow')
print(table2)


