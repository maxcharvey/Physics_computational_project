"""
This file will be used to build the relevant kernels for the games depending upon which one
is selected

Currently, the function is only set up to generate the kernel for the original Conway
Game of Life
"""

import numpy as np


def generate_kernel():
    """
    This function, named `generate_kernel`, generates a kernel matrix that is used for computing neighbor sums in grid-based games. The function currently generates a fixed 3x3 kernel matrix.

    Returns:
    - kernel: 3x3 NumPy array representing the kernel matrix used for neighbor sum computation.

    Explanation:
    1. Generates a fixed kernel matrix of size 3x3
    Each element in the kernel matrix represents the weight assigned to a neighboring cell when computing the sum of neighbors.
    2. Returns the generated kernel matrix.

    Note: The function documentation mentions that it will be updated later to take an argument 'game' that would change the kernel based on the specific game being played, but currently, this functionality is not implemented.
    """

    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    return kernel

