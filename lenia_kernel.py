"""
This is the file in which we will attempt to create the Lenia kernel
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



def lenia_kernel():

    """
        Generate a kernel resembling the Lenia cellular automaton pattern.

        Returns:
        - numpy.ndarray: Kernel resembling the Lenia pattern.

        The Lenia kernel is created by generating a bell-shaped pattern and normalizing it.
    """

    R = 13
    D = np.linalg.norm(np.asarray(np.ogrid[-R:R, -R:R], dtype="object") + 1) / R
    K = (D<1) * normal(D, 0.5, 0.15)
    kernel = K / np.sum(K)

    return kernel


if __name__ == '__main__':
    fig, ax1 = plt.subplots()
    ax1.imshow(lenia_kernel(), cmap="jet", interpolation="nearest", vmin=0)
    plt.show()