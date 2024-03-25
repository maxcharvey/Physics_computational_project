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
sigma = 0.035
T = 10


def growth_extended(u):

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

    growth_0 = (normal(u, mu, sigma)*2 -1)
    growth_1 = (normal(u, mu, sigma)*2 -1)
    growth_2 = (normal(u, mu, sigma)*2 -1)


    return growth_0, growth_1, growth_2



def lenia_extended(frame_num, img, world, kernel):

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


    kernel_0, kernel_1, kernel_2 = kernel


    u_0 = convolve2d(world[:,:,0], kernel_0, mode='same', boundary='wrap')
    u_1 = convolve2d(world[:, :, 1], kernel_1, mode='same', boundary='wrap')
    u_2 = convolve2d(world[:, :, 2], kernel_2, mode='same', boundary='wrap')


    p_0 = growth_extended(u_0)[0]
    p_1 = growth_extended(u_1)[1]
    p_2 = growth_extended(u_2)[2]


    p = np.stack([p_0, p_1, p_2], axis=-1)


    w_1 = np.array([1/3, 0.2, 2/3])
    w_2 = np.array([0.3, 0.5, 0.5])
    w_3 = np.array([0.2, 1, 0.4])

    # Perform weighted sum using dot product
    a_0 = np.dot(p, w_1)
    a_1 = np.dot(p, w_2)
    a_2 = np.dot(p, w_3)

    new_world_r = np.clip(world[:, :, 0] + (a_0 / T), 0, 1)
    new_world_g = np.clip(world[:, :, 1] + (a_1 / T), 0, 1)
    new_world_b = np.clip(world[:, :, 2] + (a_2 / T), 0, 1)

    new_world = np.stack([new_world_r, new_world_g, new_world_b], axis=-1)


    img.set_data(new_world)
    world[:] = new_world[:]

    return img

