import pandas as pd
from functools import reduce
l = lambda a, b, c: a + b + c
print(l(5, 6, 2))

def func(x):
    return lambda l : l * x
print(func(7))

double = func(4)
print(double(15))

first_lambda_str = lambda : print('Hello')
first_lambda_str()

lambda_str = lambda name : print('Hi', name)
lambda_str('Dan')

String_ = 'Findlay'
upper = lambda string : string.upper()
print(upper(String_))

format_num = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
print('Integer formatting:', format_num(10000))
print('Float formatting:', format_num(9999.4356238))

print((lambda x, y, z: x + y + z)(3, 8, 1))
print((lambda x: x if(x > 10) else 10)(5))

lst = [5, 7, 3, 55, 22, 600]
sorted(filter(lambda x: x > 10, lst))
lst2 = [10, 100, 1000, 100000, 100000]
tpl = tuple(filter(lambda x: x > 10, lst2))

print(map(lambda x: x * 10, lst2))
tpl2 = tuple(map(lambda x: x * 10, lst2))
print(tpl2)

df = pd.DataFrame({'col1': [5, 4, 3, 2, 1], 'col2': [10, 20, 30, 40, 50]})
print(df)
df['col3'] = df['col1'].map(lambda x: x * 10)
df['col4'] = df['col3'].apply(lambda x: 30 if x < 30 else x)
print(df)

lst3 = [50, 25, 70, 40, 100]
print(reduce(lambda x, y: x + y, lst3))
