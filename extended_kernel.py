"""
Here we will write the code for the extended Lenia Kernels for multi-chanel interactions
"""

import numpy as np
import matplotlib.pyplot as plt


def normal(x, mu, sigma):

    """
        Calculate the value of the normal distribution function at a given point.

        Parameters:
        - x (float or numpy.ndarray): Point(s) at which to evaluate the normal distribution.
        - mu (float): Mean of the normal distribution.
        - sigma (float): Standard deviation of the normal distribution.

        Returns:
        - float or numpy.ndarray: Value(s) of the normal distribution function at the given point(s).

        The normal distribution function is defined as:
            f(x) = exp(-((x - mu) / sigma)**2 / 2
    """

    return np.exp(-((x-mu)/sigma)**2 / 2)


def extended_kernel():

    """
    The extended kernel is actually going to return three kernels
    """

    R = 13

    D_a = np.linalg.norm(np.asarray(np.ogrid[-R:R, -R:R], dtype="object") + 1) / R
    K_a = (D_a < 1) * normal(D_a, 0.5, 0.15)
    kernel_a = K_a / np.sum(K_a)

    D_b = np.linalg.norm(np.asarray(np.ogrid[-R:R, -R:R], dtype="object") + 1) / R
    K_b = (D_b < 1) * normal(D_b, 0.0, 0.35)
    kernel_b = K_b / np.sum(K_b)

    D_c = np.linalg.norm(np.asarray(np.ogrid[-R:R, -R:R], dtype="object") + 1) / R
    K_c = (D_c < 1) * (normal(D_c, 0.0, 0.15) + normal(D_c, 0.68, 0.15))/2
    kernel_c = K_c / np.sum(K_c)

    return kernel_a, kernel_b, kernel_c

if __name__ =='__main__':
    fig, ax1 = plt.subplots(ncols=3)
    ax1=ax1.flatten()
    ax1[0].imshow(extended_kernel()[0], cmap="jet", interpolation="nearest", vmin=0)
    ax1[1].imshow(extended_kernel()[1], cmap="jet", interpolation="nearest", vmin=0)
    ax1[2].imshow(extended_kernel()[2], cmap="jet", interpolation="nearest", vmin=0)
    plt.show()

