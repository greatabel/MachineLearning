import os
from xml.etree import cElementTree as etree

from i0data import DATA_DIR

filename = os.path.join(DATA_DIR, "Posts.xml")
print("Reading from xml %s" % filename)

def parsexml(filename):
    global num_questions, num_answers

    counter = 0