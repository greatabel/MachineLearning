import numpy as np
import matplotlib.pyplot as plt


names = ["hua-n", "hua-s", "hua-middle", "hua-east"]
# names = [ "morphological-CNN-combine", "finger_restnet"]
# values = [87, 92, 95]
# gender
# values = [54, 55, 67]
# nationality
values = [69, 73, 74, 68]

plt.figure(figsize=(9, 3))


plt.subplot(131)
plt.scatter(names, values)
plt.subplot(132)
plt.bar(names, values)
plt.subplot(133)
plt.plot(names, values)

# plt.suptitle("area accuracy compare")
# plt.suptitle("gender accuracy compare")
plt.suptitle("subdivision accuracy")

plt.show()
