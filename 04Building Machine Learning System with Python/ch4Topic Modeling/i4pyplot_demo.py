import numpy as np
import matplotlib.pyplot as plt

# http://matplotlib.org/1.2.1/examples/pylab_examples/histogram_demo.html
print("help to understand subplots and hist() ")
# x = np.arange(0, 5, 0.1);
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()
num_topics_used = [10,20,20,30,30,30,40,40,40,40]
fig,ax = plt.subplots()
ax.hist(num_topics_used, np.arange(42))
ax.set_ylabel('Nr of documents')
ax.set_xlabel('Nr of topics')
fig.tight_layout()
plt.show()