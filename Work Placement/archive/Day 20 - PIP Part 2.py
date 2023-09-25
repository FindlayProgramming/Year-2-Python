import webbrowser
import requests
from collections import Counter
from mypackages import arithmetics
from mypackages import greet

print(arithmetics.add_num(4,5))
print(arithmetics.subtract(5,5))
print(arithmetics.multiple(7,7))
print(arithmetics.division(10,5))
print(arithmetics.remainder(8,5))
print(arithmetics.power(5,3))
print(greet.greet_person('Findlay', 'Duffy'))



response = requests.get('http://www.gutenberg.org/files/1112/1112.txt')

def most_common_words(text):
    split_it = text.split()
    Cnter = Counter(split_it).most_common()
    return Cnter[:10]

print(most_common_words(response.text))