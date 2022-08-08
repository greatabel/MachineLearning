import numpy as np
import matplotlib.pyplot as plt

names = ["KNN", "LG", "SVC", "ANN"]
values = [84, 86, 91, 93]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle("different ML best accuracy compare")
plt.show()
