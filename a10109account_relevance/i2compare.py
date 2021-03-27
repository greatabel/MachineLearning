import csv
import jellyfish
from termcolor import colored


def load(filepath):
	rows = []
	with open(filepath,'rt')as f:
	  data = csv.reader(f)
	  for row in data:
	        print(row, len(row))
	        rows.append(row)
	return rows


def compare(source_record, target_dataset):
	print(source_record[0],source_record[1])

	c0 = jellyfish.levenshtein_distance(u'jellyfish', u'smellyfish')
	c1 = jellyfish.jaro_distance(u'jellyfish', u'smellyfish')
	c2 = jellyfish.damerau_levenshtein_distance(u'jellyfish', u'jellyfihs')
	print(c0, c1, c2)
	
if __name__ == "__main__":
	d_rows = load('data/douban.csv')

	print(colored('数据集分割线'+'-'*30, 'red'))
	w_rows = load('data/weibo.csv')
	print(colored('compare'+'-'*30, 'red'))
	# 例子
	compare(d_rows[0], w_rows)
