"""
This is where we will now implement the Lenia rules
"""

import numpy as np
from lenia_kernel import normal
from scipy.signal import convolve2d

mu = 0.15
sigma = 0.015
T = 7.5
def growth(u):
    return normal(u, mu, sigma)*2 -1

def lenia(frame_num, img, world, kernel):

    """

    """

    u = convolve2d(world, kernel, mode='same', boundary='wrap')
    new_world = np.clip(world + 1/T * growth(u), 0, 1)


    img.set_data(new_world)
    world[:] = new_world[:]

    return img


