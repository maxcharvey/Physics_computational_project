"""
This file is for a first attempt at making the smooth life kernel
"""


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
    bounds = np.linspace(0, 1, 11)
    bounds2 = np.linspace(0, 1, 2)
    fig, ax1 = plt.subplots(ncols=2)
    ax1 = ax1.flatten()
    ax1[0].tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
    ax1[1].tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
    img1 = ax1[0].imshow(smooth_kernel()[0])
    img2 = ax1[1].imshow(smooth_kernel()[1])
    ax1[0].set_title('$K_{inner}$')
    ax1[1].set_title('$K_{outer}$')
    fig.tight_layout()
    cbar = fig.colorbar(img2, ax=ax1.ravel().tolist(), orientation='horizontal', ticks=bounds2, boundaries=bounds, pad=0.02)
    cbar.set_label('Kernel value')
    ax1[0].text(1.87, 2.48, '3x3 Grid')
    ax1[1].text(17.78, 24.20, '25x25 Grid', color='white')

    #plt.savefig('comp1', dpi=1200)

    plt.show()

