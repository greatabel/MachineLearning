import nltk.stem
# stemmer 词干分析器
s = nltk.stem.SnowballStemmer('english')
print(s.stem('graphics'))
print(s.stem('imaging'))
print(s.stem('image'))
print(s.stem('imagination'))
print(s.stem('imagine'))

from termcolor import colored
print(colored('*'*25, 'red'))
print('----verb:----')
print(s.stem('buys'))
print(s.stem('buying'))
print(s.stem('bought'))
