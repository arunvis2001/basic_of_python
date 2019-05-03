import numpy as np

from sklearn import preprocessing

#We imported a couple of packages. Let's create some sample data and add the line to this file:

input_data1 = np.array([[9, 2, 0], [0, 3, 0], [3, 0, 0]])
print('mean =', input_data1.mean(axis=0))
data = preprocessing.scale(input_data1)
print("\nMean = ", data)

# input_data = np.array([[3, -1.5, 3, -6.4], [0, 3, -1.3, 4.1], [1, 2.3, -2.9, -4.3]])
# print(input_data)
#
# data_standardized = preprocessing.scale(input_data)
# print("\nscale = ", data_standardized)
# print("\nMean = ", data_standardized.mean(axis=0))
# print("Std deviation = ", data_standardized.std(axis=0))

data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled = data_scaler.fit_transform(input_data)
print("\nMin max scaled data = ", data_scaled)