
st = set()
st1 = {'1', '2', '3', '4', '5'}
print(len(st1))
print('Does set st1 contain 5?', '5' in st1)

st1.add('6')
print(st1)

st1.update(['7', '8', '9', '10'])
print(st1)

st1.remove('3')

st1.clear()
print(st1)

del st

lst = ['o', 'p', 'r', 't', 'd']
st = set(lst)

st11 = {'1', '2', '3', '4'}
st2 = {'5', '6', '7', '8'}
st3 = st11.union(st2)
print(st3)

st_example1 = {'1', '2', '3', '4', '5'}
st_example2 = {'6', '7', '8', '9', '10'}
st_example1.update(st_example2)
print(st_example1)

st_example3 = {'1', '2', '3', '4', '5'}
st_example4 = {'1', '2'}
st_example3.intersection(st_example4)

st_example5 = {'1', '2', '3', '4'}
st_example6 = {'2', '3'}
print(st_example6.issubset(st_example5))
print(st_example5.issuperset(st_example6))

print(st_example5.difference(st_example6))
print(st_example6.difference(st3))

print(st2.symmetric_difference(st11))

st11.isdisjoint(st2)

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
first_numset = {19, 22, 24, 20, 25, 26}
second_numset = {22, 19, 24, 25, 26, 24, 25, 24}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies2 = {'Andersen Inc', 'BairesDev', 'Intetics Inc'}
It = it_companies.union(it_companies2)
print(It)

It.remove('Twitter')
print(It)
#It.discard, The difference betweem remove and discard is that unlike remove, discard does not raise an exception when an element is missing from the set.

full_set = first_numset.union(second_numset)
print(full_set)
print(first_numset.intersection(second_numset))
print(second_numset.intersection(first_numset))

print(first_numset.issubset(second_numset))
print(second_numset.issubset(first_numset))

print(first_numset.isdisjoint(second_numset))
print(second_numset.isdisjoint(first_numset))

print(first_numset.union(second_numset))
print(second_numset.union(first_numset))

print(first_numset.symmetric_difference(second_numset))

del first_numset
del second_numset


age_set = set(age)
List = print(len(age))
Set = print(len(age_set))
#str - creates a new string object from a given object. If encoding or errors are specified then the object will must expose a data buffer that would be decoded using the given encoding and error data handler.
#list - can make a series of strings, integers and floats, if no argument is given (data) then the list will be made empty. Arguments must be made iterable if specified.
#tuple - tuples have built in immutable sequences, if no arguments are given the tuple will return with an empty value. If an iterable is specified, the tuple is initialized from iterable's items.
#set - a set is meant for unordered collections of unique elements.

Final = ('I am a teacher and love people who inspire and teach methods and set to get the unique words.')
Final.split()
Final1 = set(Final)
print(Final1)
    