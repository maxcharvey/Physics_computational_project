"""
Here we are going to run some tests and try to implement Conway's game of life using a Kernel function
"""


import numpy as np
from scipy.signal import convolve2d

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

    neighbor_sum = convolve2d(world, kernel, mode='same', boundary='wrap')

    # Create temporary arrays to hold intermediate results
    alive_to_dead = ((temp_world == 1) & (((neighbor_sum / 1) < 2) | (neighbor_sum / 1 > 3)))
    dead_to_alive = ((temp_world == 0) & (neighbor_sum / 1 == 3))

    # Apply the rules simultaneously
    new_world = temp_world.copy()  # Copy the current state
    new_world[alive_to_dead] = 0  # Set alive cells with too few or too many neighbors to dead
    new_world[dead_to_alive] = 1  # Set dead cells with exactly 3 neighbors to alive

    img.set_data(new_world)
    world[:] = new_world[:]

    return img

