import numpy as np

# Numpy arrays:
# Contain only one type of data
height = [1.73, 1.68, 1.71, 1.89, 1.79]
np_height = np.array(height)
print(height)

weight = [65.4, 59.2, 63.6, 88.4, 68.7]
np_weight = np.array(weight)
print(weight)

bmi = np_weight / np_height ** 2
print(bmi)

print(bmi > 23)
print(bmi[bmi > 23])

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
print(np_2d)
print(np_2d.shape)
