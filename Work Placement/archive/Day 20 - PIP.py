import numpy
import pandas as pd
import webbrowser
import requests

lst = [5, 4, 3, 2, 1]
np_arr = numpy.array(lst)
print(np_arr)
print(len(np_arr))
print(np_arr * 2)
print(np_arr + 2)

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh',
    'https://github.com/Asabeneh',
    'https:twitter.com/Asabeneh',
]

for url in url_lists:
    webbrowser.open_new_tab(url)

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
print(response.text)

url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)
print(response)
print(response.status_code)
countries = response.json()
print(countries[:1])

