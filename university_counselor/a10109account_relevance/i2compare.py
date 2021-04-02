import csv
import jellyfish
from termcolor import colored

# https://towardsdatascience.com/calculating-string-similarity-in-python-276e18a7d33a

def load(filepath):
	rows = []
	with open(filepath,'rt')as f:
	  data = csv.reader(f)
	  for row in data:
	        # print(row, len(row))
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
		c1 = round(c1, 4)
		c2 = jellyfish.damerau_levenshtein_distance(sname, tname)
		# https://en.wikipedia.org/wiki/Hamming_distance
		c3 = jellyfish.hamming_distance(sname, tname)

		b0 = jellyfish.levenshtein_distance(s_bio, t_bio)
		b1 = jellyfish.jaro_distance(s_bio, t_bio)
		b1 = round(b1, 4)
		b2 = jellyfish.damerau_levenshtein_distance(s_bio, t_bio)
		b3 = jellyfish.hamming_distance(s_bio, t_bio)
		# print('target index=', i,'name-silimarity=', c0, c1, c2,c3,
		# 	 '\n',colored('bio-silimarity = ', 'red'), b0, b1, b2, b3)
		# 为生成实验数据，平时注释
		print('['+ str(c0)+','+ str(c1)+','+ str(c2)+','+str(c3)+','+ str(b0)+','+ str(b1)+','+ str(b2)+','+ str(b3)+','+ ' 0.999 ]')

if __name__ == "__main__":
	d_rows = load('data/douban.csv')

	print(colored('数据集分割线'+'-'*30, 'red'))

	w_rows = load('data/weibo.csv')
	print(colored('compare'+'-'*30, 'red'))
	# 例子
	for i in range(3):
		compare(d_rows[i], w_rows)
	# compare(d_rows[1], w_rows)
