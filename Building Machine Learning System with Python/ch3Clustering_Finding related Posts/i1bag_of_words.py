import collections, re

# http://stackoverflow.com/questions/15507172/how-to-get-bag-of-words-from-textual-data

texts = ['John likes to watch movies. Mary likes too.',
            'John also likes to watch football games.']
bagsofwords = [ collections.Counter(re.findall(r'\w+', txt))
            for txt in texts]
print('bagsofwords=', bagsofwords)
sumbags = sum(bagsofwords, collections.Counter())
print('sumbags=',sumbags)


