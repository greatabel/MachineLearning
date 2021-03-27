import csv

def load(filepath):
	rows = []
	with open(filepath,'rt')as f:
	  data = csv.reader(f)
	  for row in data:
	        print(row)
	return rows


if __name__ == "__main__":
	d_rows = load('data/douban.csv')
	print('-'*30)
	w_rows = load('data/weibo.csv')