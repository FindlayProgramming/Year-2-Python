import statistics
import numpy as np

lst = list()
print(len(lst))
los = []
print(len(los))
fruits = ['banana', 'orange', 'mango', 'lemon'] 
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))

lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}]

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits [-1]
second_last = fruits [-2]
print(first_fruit)
print(last_fruit)
print(second_last)

lst2 = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst2
print(first_item, '\n' , second_item, '\n', third_item, '\n', rest)

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr, '\n', fr, '\n', bg, '\n', sw, '\n', scandic, '\n', es,)

all_fruits = fruits[0:4]

orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2]
print(all_fruits, '\n', orange_and_mango, '\n', orange_mango_lemon, '\n', orange_and_lemon)

fruits[0] = 'avocado'
fruits[1] = 'apple'
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)

fruits2 = ['banana', 'orange', 'mango', 'lemon']
exist = 'banana' in fruits2
print(exist)

fruits.append('Grape Fruit')
print(fruits)

fruits.insert(2, 'apple')
print(fruits)

fruits.remove('apple')
print(fruits)

fruits.pop(2)
print(fruits)

del fruits[1:3]
print(fruits)

fruits.clear()
print(fruits)

fruits_copy = fruits.copy()
print(fruits_copy)

num = [1, 5, 6, 8, 4, 10]
zero = [0]
negative_num = [-4, -6, -9, -2]
integ = negative_num + zero + num
print(integ)

num1 = [0, 1, 5, 6]
num2 = [7, 7, 7]
num1.extend(num2)
print('Numbers:', num1)

num3 = [44, 777, 654, 889, 232]
print(num3.count(777))

num3 = [44, 777, 654, 889, 232]
print(num3.index(777))

num3 = [44, 777, 654, 889, 232]
num3.reverse()
print(num3)

num3 = [44, 777, 654, 889, 232]
num3.sort()
print(num3)

num3.sort(reverse=True)
print(num3)

lst4 = ['line', 'line1']
lst5 = ['line2', 'line3', 'line4', 'line5', 'line6']
print(len(lst5))
print(lst5[0], lst5[2], lst5[4])

mixed_data_types = ['Findlay', 18, 6.0, 'Single', '65 Wolviston Road']
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(it_companies[0], it_companies[3], it_companies[6])
it_companies[1] = 'Bioware'
print(it_companies)
it_companies.append('Digital Extremes')
print(it_companies)
it_companies.insert(3, 'FromSoftware')
print(it_companies)
print(it_companies[0].upper())
lst_str = ','.join(it_companies)
print(lst_str)
it_companies.reverse()
print(it_companies)
it_companies1 = it_companies[0:3]
it_companies2 = it_companies[4:7]
print(it_companies1, '\n', it_companies2)
js = '#'.join(it_companies)
print(js)
exist2 = 'Digital Extremes' in it_companies
print(exist2)
del it_companies[0]
print(it_companies)
del it_companies[3:5]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_back_end = front_end + back_end
full_stack = front_back_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
min_age = min(ages)
print(min_age)
max_age = max(ages)
print(max_age)
stat_avg = statistics.mean(ages)
print(stat_avg)
ages.append(min_age)
ages.append(max_age)
print(ages)
stat_median = statistics.median(ages)
print(stat_median)
def get_range(ages):
    return max(ages) - min(ages)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

stat_median_countries = statistics.median(countries)
print(stat_median_countries)
#def split_half(countries):
    #half = len(countries) >> 1
    #return countries[:half], countries[half:]
#split_half(countries)
country_list_len = len(countries)
print(country_list_len)
index = 96
first_countries_list = countries [:index]
second_countries_list = countries [index:]
print('first country list:','\n', first_countries_list)
print('second country list','\n', second_countries_list)

new_country_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *rest = new_country_list
print(first_country,'\n' + second_country,'\n' + third_country,'\n' + 'scandic countries:', rest)