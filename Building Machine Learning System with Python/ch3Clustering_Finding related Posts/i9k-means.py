# https://www.youtube.com/watch?v=_aWzGGNrcic

import sklearn.datasets
import scipy as sp

print('sklearn.datasets.get_data_home()=', sklearn.datasets.get_data_home())

all_data = sklearn.datasets.fetch_20newsgroups(subset="all")
print("Number of total posts: %i" % len(all_data.filenames))