import numpy as np
np.random.seed()

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2:
    step = step - 1
elif dice >= 3 and dice <= 5:
    step += 1
else:
    step = step + np.random.randint(1, 7)

# Print out dice and step
print(dice, step)

coin = np.random.randint(0, 2)  # Randomly generate 0 or 1
print(coin)
if coin == 0:
    print("heads")
else:
    print("tails")
