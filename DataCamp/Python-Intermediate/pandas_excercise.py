import pandas as pd
import numpy as np

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan',
         'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
cars = pd.DataFrame(cars_dict)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

# selecting data
# .iloc works with index ex: [:,[1,2]] | [[0,1],[1]]
# .loc works with words ex: [["USA", "RU", "CHINA"], ["country","cars_per_cap"]]
# print(cars[]) panda series
# print(cars[[]]) panda dataframe
print(cars.loc[['US', 'JPN'], ['cars_per_cap']])
print(cars.iloc[:, [1]])

# Operators pandas
car_maniac = cars[cars['cars_per_cap'] > 500]

# Print car_maniac
print(car_maniac)

# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[np.logical_and(
    cars['cars_per_cap'] > 100, cars['cars_per_cap'] < 500)]


# Print medium
print(medium)
