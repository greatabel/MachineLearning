from scipy.spatial import distance
import numpy as np

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html#scipy.spatial.distance.cdist
coords = [(35.0456, -85.2672),
          (35.1174, -89.9711),
          (35.9728, -83.9422),
          (36.1667, -86.7833)
          ]

result = distance.cdist(coords, coords, 'euclidean')
print(coords, '#'*20,'\n',
    result)

a = np.array([[0, 0, 0],
              [0, 0, 1],
              [0, 1, 0],
              [0, 1, 1],
              [1, 0, 0],
              [1, 0, 1],
              [1, 1, 0],
              [1, 1, 1]])
b = np.array([[ 0.1,  0.2,  0.4]])
result = distance.cdist(a, b, 'cityblock')
print('\n\n', result)