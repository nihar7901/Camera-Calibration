import matplotlib.pyplot as plt
import numpy as np


def create_checkerboard(rows, cols):
    checkerboard = np.zeros((rows, cols))
    checkerboard[::2, ::2] = 1  
    checkerboard[1::2, 1::2] = 1  
    return checkerboard


plt.figure(figsize=(8.27, 11.69))  # A4 size in inches
checkerboard = create_checkerboard(7, 11)

# Plot the checkerboard
plt.imshow(checkerboard, cmap='binary', interpolation='nearest')


# Saving the checkerboard image
plt.savefig('checkerboard_11x7.png', dpi=300, bbox_inches='tight')

