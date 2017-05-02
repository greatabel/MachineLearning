import os


from operator import itemgetter
from xml.etree import cElementTree as etree

from i0data import DATA_DIR

filename = os.path.join(DATA_DIR, "Posts.xml")
print("Reading from xml %s" % filename)

def parsexml(filename):
    global num_questions, num_answers

    counter = 0
    it = map(itemgetter(1),
         iter(etree.iterparse(filename, events=('start',))))

    root = next(it)  # get posts element
    for elem in it:
        if counter % 1000 == 0:
            print("Processed %i <row/> elements" % counter)

        counter += 1

        if elem.tag == 'row':
            if counter % 100 == 0:
                print(elem.get('CreationDate'))
    print('counter = ', counter)

parsexml(filename)