import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def stop_words():
    stop_words = set(stopwords.words('english'))
    f = open('C:\\Users\\duffy.findlay\\Desktop\\Work Placement Files and Tasks\\melina_trump_speech.txt')
    line = f.read()
    words = line.split()
    for r in words:
        if not r in stop_words:
            appendFile = open('C:\\Users\\duffy.findlay\\Desktop\\Work Placement Files and Tasks\\Filtered_words.txt', 'a')
            appendFile.write(" "+r)
            appendFile.close()