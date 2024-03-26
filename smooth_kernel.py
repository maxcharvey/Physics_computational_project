"""
This file is for a first attempt at making the smooth life kernel
"""

#TODO: May need to write a different function that makes a circular kernel - may need to find out exactly
# which larger circular kernel is actually used the for the smooth game of life


import numpy as np
import matplotlib.pyplot as plt


def get_circular_kernel(diameter):

    """
    Generates a circular kernel of the specified diameter.

    Parameters:
    - diameter (int): Diameter of the circular kernel.

    Returns:
    - numpy.ndarray: Circular kernel.

    This function demonstrates how to create a circular kernel using numpy.
    """

    mid = (diameter - 1) / 2
    distances = np.indices((diameter, diameter)) - np.array([mid, mid])[:, None, None]
    kernel = ((np.linalg.norm(distances, axis=0) - mid) <= 0).astype(int)

    return kernel


def smooth_kernel():

    """
    Defines a smooth kernel for the Smooth Game of Life.

    Returns:
    - tuple: Tuple containing two kernels, kernel_a and kernel_b.

    This function defines two kernels for the Smooth Game of Life.
    - kernel_a is a 3x3 kernel with all elements set to 1, except for the center, which is 0.
    - kernel_b is a circular kernel with a diameter of 25, generated using the get_circular_kernel function.

    """

    kernel_a = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    kernel_b = get_circular_kernel(25)

    return kernel_a, kernel_b

if __name__ == '__main__':
    fig, ax1 = plt.subplots(ncols=2)
    ax1=ax1.flatten()
    ax1[0].imshow(smooth_kernel()[0])
    ax1[1].imshow(smooth_kernel()[1])
    plt.show()