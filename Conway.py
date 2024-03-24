"""
This file is an implementation of Conway's game of life, the basic precursor to Lenia
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Function to update the state of the grid for each generation
def update(frameNum, img, grid, N):

    """
    Updates the state of the grid for each generation according to Conway's Game of Life rules.

    Parameters:
    - frameNum: The current frame number in the animation.
    - img: The image object representing the grid.
    - grid: The 2D NumPy array representing the current state of the grid.
    - N: The size of the grid (N x N).

    Returns:
    - The updated image object.
    """

    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Compute the sum of the neighbors' states (toroidal boundary conditions)
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]) / 255)
            # Apply Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    # Update the data for the animation
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

# Set the size of the grid
N = 100
# Set the states of the cells (0 for dead, 255 for alive)
ON = 255
OFF = 0
# Probability of a cell being alive at the start
probability_alive = 0.2

# Create a random initial grid
grid = np.random.choice([ON, OFF], N*N, p=[probability_alive, 1-probability_alive]).reshape(N, N)

# Set up the animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N), frames=100, interval=50, save_count=50)

plt.show()
