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
from stop_words import stop_words as sw

#Level 2: 7. (Will have to come back to)

def clean_text(text):
    text = ''
    text = text.lower()
    text = re.sub('\[.*?]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def remove_support_words(text):
    return [word for word in text.split() if word not in sw]


def read_file(fname):
    try:
        with open(fname, 'r', encoding='UTF8') as f:
            data = remove_support_words(clean_text(f.read))
        return data
    except IOError:
        print('Error opening or reading input file:', fname)
        sys.exit()

def count_frequency(word_list):
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word] + 1
        else:
            D[new_word] = 1
    return D
        
def word_frequency_in_file(fname):
    word_list = read_file(fname)
    freq_mapping = count_frequency(word_list)
    print(
        'File',
        fname,
        ':',
    )
    print(len(freq_mapping), 'distinct words')
    return freq_mapping

def dotProduct(D1, D2):
    Sum = 0.0
    for key in D1:
        if key in D2:
            Sum += D1[key] * D2[key]
    return Sum

def vector_angle(D1, D2):
    numerator = dotProduct(D1, D2)
    denominator = math.sqrt(dotProduct(D1, D1) * dotProduct(D2, D2))
    
    return math.acos(numerator / denominator)

def doc_similarity(fname_1, fname_2):
    sorted_word_list_1 = word_frequency_in_file(fname_1)
    sorted_word_list_2 = word_frequency_in_file(fname_2)
    distance = (vector_angle(sorted_word_list_1, sorted_word_list_2) * 180)
    print("Distance between documents: % 0.2f (degrees)" % distance)
doc_similarity('C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\melina_trump_speech.txt', 'C:\\Users\\duffy.findlay\\Documents\\FinWork\\Task 1 13\\07\\Python Guide\\michelle_obama_speech.txt')

#Not finished / Still solving