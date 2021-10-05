import os
import pickle
import pprint
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import csv


def csv_reader(filename, directory="./"):
	with open(os.path.join(directory, filename), newline="") as csvfile:
		reader = csv.reader(csvfile, delimiter="\n", quotechar=",")
		mylist = []
		for row in reader:
			if len(row)>0 and row[0] != '"':
				mylist.append(row[0].split(","))
		return mylist



def write_to_csv(path, mylist):
    with open(path, 'w', newline='') as myfile:
         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
         for item in mylist:
         	wr.writerow(item)