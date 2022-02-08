family: list = [1.1, 31, 43,1.211, 12.,3]
for height in family:
    print(height)

# get index for loop python
for index, height in enumerate(family):
    print(f"index[{index}]: height{height}")

word = "family"
for c in word:
    print(f"{c.capitalize()}",end="")

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for room, mtr in house:
    print("the " + str(room) + "is " + str(mtr) + " sqm")

stupid_shit = {
    "country_x": 10,
    "country_y": 20,
    "country_z": 30
}
for key, value in stupid_shit.items():
    print(f"key:{key}-----value:{value}")

# Import numpy as np
import numpy as np
np_height = np.array([21,321,31,31,431,31])
# For loop over np_height
for height in np_height:
    print(str(height) + " inches")

np_baseball = np.array([[1,31,13,31,31],[31,31,31,21,12]])
# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)

# Import cars data
import pandas as pd
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

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab) + ": " + str(row['cars_per_cap']))
# Code for loop that adds COUNTRY column
# for lab, row in cars.iterrows():
#     cars.loc[lab, "COUNTRY"] = row['country'].upper()

#Does the same as the for loop before but is more eficient this way
cars["COUNTRY"] = cars['country'].apply(str.upper)

# Print cars
print(cars)
