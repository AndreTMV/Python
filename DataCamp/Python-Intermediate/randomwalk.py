import numpy as np
import matplotlib.pyplot as plt
# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100):
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1, 7)

    # Determine next step
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Plot random_walk
# The first list you pass is mapped onto the x axis and the second list is mapped onto the y axis.

# If you pass only one argument, Python will know what to do and will use the index of the list to map onto the x axis, and the values in the list onto the y axis.
plt.plot(random_walk)
plt.show()
