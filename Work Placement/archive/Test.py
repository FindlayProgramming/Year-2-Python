def func_arg(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(func_arg(7, 70, 777))

array = [1, 2, 3, 4, 5]
for i in range(len(array) //2):
    array[i], array[-1 - i] = array[-1 - i], array[i]
    print(array)

#factorial = 1
    #num = whole
    #if num < 0:
        #print('Factorial number cannot be applied to negative numbers')
    #elif num == 0:
        #print('The factorial of 0 is 1')
    #else:
        #for i in range(1, num + 1):
            #factorial = factorial * i
            #print('The factorial of', num, factorial)
            
#def clean_text(text):
    #text = text.lower()
    #text = re.sub('\[.*?]', '', text)
    #text = re.sub('https?://\S+|www\.\S+', '', text)
    #text = re.sub('<.*?>+', '', text)
    #text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    #text = re.sub('\n', '', text)
    #return text

#def remove_support(text):
    #return [word for word in text.split() if word not in sw]