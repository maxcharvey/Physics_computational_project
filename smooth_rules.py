"""
This is the first attempt at writing the rules for the smooth game of life
"""

import numpy as np
from scipy.signal import convolve2d

def smooth(frame_num, img, world, kernel):

    """
    Apply smooth rules for the Game of Life.

    Parameters:
    - frame_num (int): Frame number.
    - img (numpy.ndarray): Image data.
    - world (numpy.ndarray): Current state of the Game of Life world.
    - kernel (tuple): Tuple containing two 2D arrays representing the small and large kernels for convolution.

    Returns:
    - numpy.ndarray: Updated image data after applying smooth rules.

    Smooth rules are applied to the Game of Life world using convolution with specified kernels.
    Rules are applied based on fractions derived from the convolution results.
    The new state is determined by simultaneous application of rules and setting all other cells to 0.

    Example:
    smooth(1, img, world, (kernel_small, kernel_large))
    """

    kernel_s, kernel_l = kernel

    neighbor_sum_s = convolve2d(world, kernel_s, mode='same', boundary='wrap')
    neighbor_sum_l = convolve2d(world, kernel_l, mode='same', boundary='wrap')


    # Now we need to apply the smooth life rules
    fract_s = neighbor_sum_s / (np.sum(kernel_s)*255)
    fract_l = neighbor_sum_l / (np.sum(kernel_l)*255)


    # Apply the rules simultaneously and set all other cells to 0
    new_world = np.where(((fract_s >= 0.5) & (fract_l >= 0.26) & (fract_l <= 0.46)) | (
                (fract_s < 0.5) & (fract_l >= 0.27) & (fract_l <= 0.36)), 255, 0)

    img.set_data(new_world)
    world[:] = new_world[:]

    return img

