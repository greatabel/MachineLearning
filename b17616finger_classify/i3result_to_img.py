import numpy as np
import matplotlib.pyplot as plt


names = ["img-processing", "cnn", "morphological-CNN-combine"]
# values = [87, 92, 95]
# gender
# values = [54, 55, 67]
# nationality
values = [76, 75, 80]

plt.figure(figsize=(9, 3))


plt.subplot(131)
plt.scatter(names, values)
plt.subplot(132)
plt.bar(names, values)
plt.subplot(133)
plt.plot(names, values)

# plt.suptitle("area accuracy compare")
# plt.suptitle("gender accuracy compare")
plt.suptitle("nationality accuracy compare")

plt.show()