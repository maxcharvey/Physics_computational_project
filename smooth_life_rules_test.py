"""
This is the first attempt at writing the rules for the smooth game of life
"""

import numpy as np
from scipy.signal import convolve2d

def smooth(frame_num, img, world, kernel_s, kernel_l):

    """
    This function will apply the rules for the smooth game of life
    """

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

