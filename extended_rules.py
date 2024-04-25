"""
Here we will implement the updated lenia rules to expanded into 'Extended Lenia'
"""


import numpy as np
from lenia_kernel import normal
from scipy.signal import convolve2d
import matplotlib.pyplot as plt


mu = 0.15
sigma = 0.035
T = 10
shape = 3 #The shape used for generating random arrays for the weight functions



#inputs = np.asarray([0.8278459354506137, 0.5000109152390321, 0.8100110078208058, 0.28657741608469534, 0.46776806268051796, 0.5664957092976507, 0.24916729217681577, 0.1963648170169402, 0.16609675537427926, 0.9951227994940144, 0.6103420344708071, 0.3140492762389717])
inputs = np.asarray([])



if len(inputs) == 0:
    a_g = np.random.rand()
    b_g = np.random.rand()
    c_g = np.random.rand()
    w_1 = np.random.uniform(0, 1, size=shape)
    w_2 = np.random.uniform(0, 1, size=shape)
    w_3 = np.random.uniform(0, 1, size=shape)
else:
    a_g = inputs[0]
    b_g = inputs[1]
    c_g = inputs[2]
    w_1 = np.asarray([inputs[3], inputs[4], inputs[5]])
    w_2 = np.asarray([inputs[6], inputs[7], inputs[8]])
    w_3 = np.asarray([inputs[9], inputs[10], inputs[11]])


print(f'np.asarray([{a_g}, {b_g}, {c_g}, {w_1[0]}, {w_1[1]}, {w_1[2]}, {w_2[0]}, {w_2[1]}, {w_2[2]}, {w_3[0]}, {w_3[1]}, {w_3[2]}])')


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

    growth_0 = a_g*(normal(u, mu, sigma)*2 -1)
    growth_1 = b_g*(normal(u, mu, sigma)*2 -1)
    growth_2 = c_g*(normal(u, mu, sigma)*2 -1)


    return growth_0, growth_1, growth_2

def extended(frame_num, img, world, kernel):

    """
    Update the Lenia world based on the convolution with the given kernel.

    Parameters:
    - frame_num (int): Frame number of the animation.
    - img (matplotlib.image.AxesImage): Image object representing the current state of the world.
    - world (numpy.ndarray): Array representing the current state of the Lenia world.
    - kernel (tuple): Tuple containing three kernels used for convolution.

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


    #w_1 = np.array([1/3, 0.2, 2/3])
    #w_2 = np.array([0.3, 0.5, 0.5])
    #w_3 = np.array([0.2, 1, 0.4])

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

if __name__ == '__main__':
    fig, ax = plt.subplots()
    t = np.linspace(0, 1, 1000)
    ax.plot(t, growth_extended(t)[0], c='r', label='Red Channel')
    ax.plot(t, growth_extended(t)[1], c='g', label='Green Channel')
    ax.plot(t, growth_extended(t)[2], c='b', label='Blue Channel')
    ax.set_xlabel('$U$')
    ax.set_ylabel('$P$')
    ax.axhline(0, c='k', linestyle='--', alpha=0.5)
    ax.legend()
    plt.show()

