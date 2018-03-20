import numpy as np

vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])

assert np.linalg.norm(vec1 - vec2) == np.sqrt(np.sum(np.square(vec1 - vec2))),\
        "should be same"
