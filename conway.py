"""
Here we are going to run some tests and try to implement Conway's game of life using a Kernel function
"""


import numpy as np


def conway(frame_num, img, world, kernel):

    """
    This function, named `conway`, applies one step of Conway's Game of Life rules to the given world/grid.

    Parameters:
    - frame_num: Represents the frame number, but it's not used within the function.
    - img: Matplotlib image object used for visualization.
    - world: 2D NumPy array representing the current state of the world/grid.
    - kernel: 3x3 NumPy array representing the kernel for computing neighbor sums.

    Returns:
    - new_world: 2D NumPy array representing the new state of the world/grid after applying the rules.

    Explanation:
    1. Creates a copy of the current world/grid called temp_world.
    2. Computes the sum of neighbors for each cell in the world/grid using the provided kernel.
    3. Applies Conway's rules to update the state of each cell based on the sum of its neighbors and its own state.
    4. Updates the visualization image (`img`) with the new world/grid state.
    5. Updates the original world/grid with the new state.
    6. Returns the new state of the world/grid.
    """

    temp_world = world.copy()

    neighbor_sum = np.zeros_like(world)
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbor_sum += np.roll(world, (i, j), axis=(0, 1)) * kernel[i + 1, j + 1]

    # Apply Conway's rules based on the sum and the state of the current cell
    new_world = np.where((temp_world == 255) & (((neighbor_sum/255) < 2) | (neighbor_sum/255 > 3)), 0, temp_world)
    new_world = np.where((temp_world == 0) & (neighbor_sum/255 == 3), 255, new_world)

    img.set_data(new_world)
    world[:] = new_world[:]

    return img

