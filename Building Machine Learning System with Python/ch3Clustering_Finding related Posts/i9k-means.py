# https://www.youtube.com/watch?v=_aWzGGNrcic

import sklearn.datasets
import scipy as sp
from termcolor import colored

print('sklearn.datasets.get_data_home()=', sklearn.datasets.get_data_home())

all_data = sklearn.datasets.fetch_20newsgroups(subset="all")
print("Number of total posts: %i" % len(all_data.filenames))
print(all_data.filenames[0:3])

print(colored('*'*25, 'magenta'),'target_names')
print(all_data.target_names, '\n'*3)

#  选取一些新闻组进行 训练
groups = [
    'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware',
    'comp.sys.mac.hardware', 'comp.windows.x', 'sci.space']
train_data = sklearn.datasets.fetch_20newsgroups(subset="train",
                                                 categories=groups)
print("Number of training posts in tech groups:", len(train_data.filenames))