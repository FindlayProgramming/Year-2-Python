import sys

import os
import json
import csv
import re
import string
import math
import csv
import xml.etree.ElementTree as ET
from collections import Counter

#Txt files:

#with open('C:\\Users\\duffy.findlay\\Desktop\\Work Placement Files and Tasks\\New Text Document.txt', mode='ar', encoding='utf-8') as f:
    #txt = f.read()
    #print(type(txt))
    #print(txt)
    #f.close()

#with open('C:\\Users\\duffy.findlay\\Desktop\\Work Placement Files and Tasks\\New File Through Python', mode='w', encoding='utf-8') as s:
    #s.write('New text through python!')
    #s.read()
    #s.close()

#with open('C:\\Users\\duffy.findlay\\Downloads\\Pseudo.txt', mode='a', encoding='utf-8') as file:
    #file.write('Appended content.')
    #file.close()

#Deleting files:

#os.remove('C:\\Users\\duffy.findlay\\Downloads\\Pseudo.txt')

#if os.path.exists('C:\\Users\\duffy.findlay\\Downloads\\Example.txt'):
    #os.remove('C:\\Users\\duffy.findlay\\Downloads\\Example.txt')
#else:
    #print('File does not exist.')

#Json:

example = '''{
    "name": "Findlay",
    "skills": ["Python", "HTML", "CSS"],
    "country": "UK"
}'''

example_dct = json.loads(example)
print(type(example_dct))
print(example_dct)
print(example_dct['skills'])

example_json = json.dumps(example, indent=4)
print(type(example_json))
print(example_json)

with open('C:\\Users\\duffy.findlay\\Desktop\\Work Placement Files and Tasks\\examplefile.json', 'w', encoding='utf-8') as j:
    json.dump(example, j, ensure_ascii=False, indent = 4)

#CSV:

#with open('C:\\Users\\duffy.findlay\\Desktop\\Work Placement Files and Tasks\\Example.csv') as csvfile:
    #csv_reader = csv.reader(csvfile, delimiter=',')
    #line_count = 0
    #for row in csv_reader:
        #if line_count == 0:
           #print(f'Column names are:{",".join(row)}') 
           #line_count += 1
        #else:
            #print(
                #f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[1]}, {row[2]}.')
            #line_count += 1
    #print(f'Number of lines: {line_count}')   

#Excel (xlsx):

#excel_example = xlrd.open_workbook('example.xls')
#print(excel_book.nsheets)
#print(excel_book.sheet_names)

#XML:

tree = ET.parse('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\XML Example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field:', child.tag)
    
#Exercise: Level 1a:
with open('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\obama_speech - Copy.txt', 'rt') as f:
    every_line = f.readlines()
    print('Number of lines:', len(every_line))
    f.close()

with open('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\obama_speech - Copy.txt', 'rt') as f:
    wordcount = Counter(f.read().split())
    for item in wordcount.items(): 
        print('{}\t{}'.format(*item))
        
#Exercise: level 1b:
with open('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\michelle_obama_speech.txt', 'rt') as f:
    every_line = f.readlines()
    print('Number of lines:', len(every_line))
    f.close()
    
with open('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\michelle_obama_speech.txt', 'rt') as f:
    wordcount = Counter(f.read().split())
    for item in wordcount.items(): 
        print('{}\t{}'.format(*item))

#Exercise: level 1c:
with open('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\donald_speech.txt', 'rt') as f:
    every_line = f.readlines()
    print('Number of lines:', len(every_line))
    f.close()
    
with open('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\donald_speech.txt', 'rt') as f:
    wordcount = Counter(f.read().split())
    for item in wordcount.items(): 
        print('{}\t{}'.format(*item))

#Exercise: level 1d:
with open('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\melina_trump_speech.txt', 'rt') as f:
    every_line = f.readlines()
    print('Number of lines:', len(every_line))
    f.close()
    
with open('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\melina_trump_speech.txt', 'rt') as f:
    wordcount = Counter(f.read().split())
    for item in wordcount.items(): 
        print('{}\t{}'.format(*item))

#Exercise: level 1: 2:
#with open('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\countries_data.json', 'rb', 10) as f:
    #countries = json.load(f)
    #print(type(countries))
    #for country in countries:
        #print(type(country))
        #for language in country['languages']:
           # c = Counter(items['languages'] for items in countries)
            #print(c)
            #print(language)
#f.close()

#with open('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\countries_data.json', 'rb') as f:
    #countries = json.load(f)
    #languages = Counter(country['languages'] for country in countries)
        #print("{} count: {}".format(k,v))
#f.close()
#Review later.

#Exercise Level 1: 3.
def sort_dict(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))

def most_populated_countries(value):
    with open('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\countries_data.json', encoding='UTF8') as f:
        json_list = json.load(f)
        populations = {}
        final = []
        for i in json_list:
            populations[i['name']] = i['population']
        populations = sort_dict(populations, True)
        for data in list(populations.items())[:value]:
            final.append({'Country': data[0], 'Population': data[1]})
        f.close()
        return final
print(most_populated_countries(3))
#Needed help with this one as it is difficult to understand for now. Will take some time to fully understand how to do these exercises as they use lambda. I am going to review the work done previously as well.

#Exercises: Level 2: 4.

def listed_words(filename):
    output = []
    with open(filename, 'r', encoding='UTF8') as file:
        for line in file:
            for word in line.split():
                output.append(word)
    return list(set(output))
                

def email_check(word):
    if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', word):
        return True
    else:
        return False

def email_extraction(filename):
    words = listed_words(filename)
    email_list = []
    
    for word in words:
        if email_check(word):
            email_list.append(word)
    return email_list
print(email_extraction('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\email_exchanges_big.txt'))

#Level 2: 5/6/8.
def common_words(filename, value):
    text = open(filename).read()
    split_it = text.split()
    Count = [(sub[1], sub[0]) for sub in Counter(split_it).most_common()]
    return Count[:value]
print(common_words(r'C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\michelle_obama_speech.txt', 10))
print(common_words(r'C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\donald_speech.txt', 10))
print(common_words(r'C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\melina_trump_speech.txt', 10))
print(common_words(r'C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\obama_speech - Copy.txt', 10))
print(common_words(r'C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\romeo_and_juliet.txt', 10))

#level 2: 9.
def hacker_news_count(filename):
    csvFile = csv.reader(open(filename, mode='r'))
    count_a = 0
    count_b = 0
    count_c = 0
    for lines in csvFile:
        plain_text_line = ''.join(lines)
        if 'python' in plain_text_line or 'Python' in plain_text_line:
            count_a += 1
        if (
            'JavaScript' in plain_text_line
            or 'Javascript' in plain_text_line
            or 'javascript' in plain_text_line
        ):
            count_b += 1
        if not (not ('Java' in plain_text_line) or 'Javascript' in plain_text_line):
            count_c += 1
    print(count_a, count_b, count_c)
hacker_news_count(r'C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\hacker_news.csv')

#Will have to revisit this file to fully understand how to complete this challenges without much help.
            