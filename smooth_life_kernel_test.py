"""
This file is for a first attempt at making the smooth life kernel
"""

#TODO: Need to write own function that makes a circular kernel - may need to find out exactly
# which larger circular kernel is actually used the for the smooth game of life


import numpy as np


def get_circular_kernel(diameter):

    """
    This is an example of how to make a circular kernel
    """

    mid = (diameter - 1) / 2
    distances = np.indices((diameter, diameter)) - np.array([mid, mid])[:, None, None]
    kernel = ((np.linalg.norm(distances, axis=0) - mid) <= 0).astype(int)

    return kernel


def smooth_kernel():

    """
    Defines a smooth kernel for the smooth game of life of size n
    """

    kernel_a = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    kernel_b = get_circular_kernel(25)

    return kernel_a, kernel_b

