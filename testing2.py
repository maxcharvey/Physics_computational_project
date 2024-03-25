"""
Here we will implement the updated lenia rules to expanded into 'Extended Lenia'
"""

"""
This is where we will now implement the Lenia rules
"""

import numpy as np
from lenia_kernel import normal
from scipy.signal import convolve2d

mu = 0.15
sigma = 0.015
T = 10


#TODO: eventually this growth function will have to be different or each channel and each kernel
# but this will be addressed at a later date...

def growth(u):

    """
        Calculate the growth factor based on the input value(s) using a normalized normal distribution.

        Parameters:
        - u (float or numpy.ndarray): Input value(s) at which to evaluate the growth factor.

        Returns:
        - float or numpy.ndarray: Growth factor value(s) calculated based on the input.

        The growth factor is calculated using a normalized normal distribution function with parameters mu and sigma.
        The formula for the growth factor is:
            growth(u) = 2 * normal(u, mu, sigma) - 1

        This function is typically used in cellular automata simulations, where it influences the evolution of the system.
    """

    return normal(u, mu, sigma)*2 -1



def lenia(frame_num, img, world, kernel):

    """
    Update the Lenia world based on the convolution with the given kernel.

    Parameters:
    - frame_num (int): Frame number of the animation.
    - img (matplotlib.image.AxesImage): Image object representing the current state of the world.
    - world (numpy.ndarray): Array representing the current state of the Lenia world.
    - kernel (numpy.ndarray): Kernel used for convolution.

    Returns:
    - matplotlib.image.AxesImage: Updated image object representing the modified world state.

    This function performs convolution of the Lenia world with the given kernel,
    computes the new state of the world based on Lenia growth rules, and updates
    the image object accordingly.
    """

    u = convolve2d(world, kernel, mode='same', boundary='wrap')
    new_world = np.clip(world + 1/T * growth(u), 0, 1)


    img.set_data(new_world)
    world[:] = new_world[:]

    return img




