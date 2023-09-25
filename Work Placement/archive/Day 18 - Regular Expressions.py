import re
from collections import Counter
#sentence = 'Python is a dynamic programming language.'
#match = re.match('Python', sentence, re.I)
#print(match)
#span = match.span()
#print(span)
#s, e = span
#print(s, e)
#substr = sentence[s:e]
#print(substr)

sentence = '''Python is an easy programming language to grasp when compared to other programming languages but does come with its drawbacks.'''
match = re.search('is an easy programming language', sentence, re.I)
print(match)
span = match.span()
print(span)
s, e = span
print(s, e)
substring = sentence[s:e]
print(substring)

matches = re.findall('programming', sentence, re.I)
print(matches)

matches1 = re.findall('Python|python', sentence)
print(matches1)

match_replace = re.sub('Python|python', 'Dart', sentence, re.I)
print(match_replace)

random_sentence = 'H%i I %a%%m F%i%%n%d%%l%a%%y'

match_replace1 = re.sub('%', '', random_sentence)
print(match_replace1)

print(re.split('\n', sentence))

regex_pattern = r'A[Ii]'
sentence2 = 'AI has really taken off over the years. Ai will come with a lot of benefits but also some drawbacks.'
matched = re.findall(regex_pattern, sentence2)
print(matched)

regex_patt = r'[Vv]r|[Aa]r'
sentence3 = 'Vr has become well known over the years but has yet to be fully applied as vr still needs to become more developed. Ar will take time to ever really develop as ar is far more advanced that vr.'

regex_pattern3 = r'\d'
sentence4 = 'The date is August 10, 2023.'
matched1 = re.findall(regex_pattern3, sentence4)

regex_pattern1 = r'[a].'
sentence5 = '''Ar and Vr are similar concepts.'''
matched2 = re.findall(regex_pattern1, sentence5)
print(matched2)

regex_pattern2 = r'[a].+'
matched3 = re.findall(regex_pattern2, sentence5)
print(matched3)

regex_pattern2 = r'[a].*'
matched3 = re.findall(regex_pattern2, sentence5)
print(matched3)

mail = '''Mail mail M-ail'''
regexpattern4 = r'[Mm]-?ail'
matched4 = re.findall(regexpattern4, mail)
print(matched4)

#regexpattern5 = r'\d{1, 4}'
#matched5 = re.findall(regexpattern5, sentence4)
#print(matched5)

#regexpattern6 = r'^This'
#matched6 = re.findall(regexpattern6, sentence4)
#print(matched6)

#regexpattern7 = r'[^A-Za-z ]+'
#matched7 = re.findall(regexpattern7, sentence4)
#print(matched7)

#Exercise: Level 1: 1.
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
s = re.findall(r'\s(\w+)$', paragraph)
print(s) #Will review again at a later date.

#print('Original list:', paragraph)
#frequency = defaultdict(int)
#for sub in paragraph:
    #for word in sub.split():
        #frequency[word] += 1

#res = max(frequency, key=frequency.get)

#print('The word that occurs the most often:', res)

#Exercise: Level 1: 2.
points = ['-12', '-4', '-3', '-1', '0', '2', '4', '8']
print('Original string:', points)
extracted_num = ''
for i in points:
    if i.isdigit():
        extracted_num = extracted_num + i 
o = '-1', '-2', '-3', '-4'.isdigit()      
ls = abs(-12 - 8)
print(ls)
print('Extracted:' + extracted_num, 'distance:', ls) #May review later.

#Exercise: Level 2.
valid_variable = ('first_name')
print(valid_variable.isidentifier())
valid_variable1 = ('first-name')
print(valid_variable1.isidentifier())
valid_variable2 = ('1first_name')
print(valid_variable2.isidentifier())
valid_variable3 = ('firstname')
print(valid_variable3.isidentifier())

#Exercise: Level 3.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
matches2 = re.sub(r'[%$#&@;]', '', sentence)
print(matches2)
split_it = matches2.split()
Counter = Counter(split_it)
most_frequent = Counter.most_common(3)
print(most_frequent)
