import csv
import jellyfish
from termcolor import colored

# https://towardsdatascience.com/calculating-string-similarity-in-python-276e18a7d33a

def load(filepath):
	rows = []
	with open(filepath,'rt')as f:
	  data = csv.reader(f)
	  for row in data:
	        print(row, len(row))
	        rows.append(row)
	return rows


def compare(source_record, target_list):
	sname = source_record[2]
	s_bio = source_record[4]
	print(sname, s_bio, '#'*10)
	for i in range(0, len(target_list)):
		target = target_list[i]
		tname = target[2]
		t_bio = target[4]
		c0 = jellyfish.levenshtein_distance(sname, tname)
		c1 = jellyfish.jaro_distance(sname, tname)
		c2 = jellyfish.damerau_levenshtein_distance(sname, tname)
		b0 = jellyfish.jaro_distance(s_bio, t_bio)
		print('target index=', i, 'name silimarity=', c0, c1, c2, 'bio silimarity=', b0)

if __name__ == "__main__":
	d_rows = load('data/douban.csv')

	print(colored('数据集分割线'+'-'*30, 'red'))
	w_rows = load('data/weibo.csv')
	print(colored('compare'+'-'*30, 'red'))
	# 例子
	compare(d_rows[0], w_rows)
