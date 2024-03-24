"""
This script is going to be used for generating the initial worlds based upon a number of given parameters
This will enable the world to be setup for:
- Conways game of life
- Smooth life
- Lenia
- Extended Lenia

In order to do this the following operations need to be completed
2. The world of a certain size needs to be generated and the initial conditions need to be applied
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


#TODO: also need to alter these functions so that eventually they can take a defined input if you want to demonstrate a
# certain structure such as a glider - this may have to just be done with a separate function in main.py so that you can
# either select to make a random world or look at a specific structure


def generate_world(n, p, game):
    """
    This function generates the initial state of the world/grid for the specified game.

    Parameters:
    - n: Integer, the size of the world/grid (n x n).
    - p: Float, the parameter determining the initial state probabilities.
    - game: Integer, specifying the type of game:
      - 0: Conway's Game of Life
      - 1: Smooth Life
      - 2: Lenia
      - 3: Extended Lenia

    Returns:
    - grid: 2D NumPy array, representing the initial state of the world/grid.

    Notes:
    - For Conway's Game of Life, the initial state consists of randomly distributed alive and dead cells based on the given probability.
    - For Smooth Life, Lenia, and Extended Lenia, the initial state is generated based on a normal distribution around the specified probability.
    - If an invalid game identifier is provided, a warning is printed, and Conway's Game of Life is assumed by default.
        """


    # here we need to create a normal distribution around some value such that the integral = p
    a = np.linspace(0, 1, 256)
    b = norm.pdf(a, p, 0.15)
    norm_normal = b / sum(b)


    if game == 0: # For Conway's game of life
        probability_alive = p
        initial_state_options = [255, 0]
        initial_state_probabilities = [probability_alive, 1-probability_alive]
    elif game == 1: # For smooth life
        initial_state_options = np.linspace(0, 255, 256)[::-1]
        initial_state_probabilities = norm_normal[::-1]
    elif game == 2: # For Lenia
        initial_state_options = np.linspace(0, 255, 256)[::-1]
        initial_state_probabilities = norm_normal[::-1]
    elif game == 3: # For extended Lenia
        initial_state_options = np.linspace(0, 255, 256)[::-1]
        initial_state_probabilities = norm_normal[::-1]
    else:
        probability_alive = p
        initial_state_options = [255, 0]
        initial_state_probabilities = [probability_alive, 1 - probability_alive]
        print("You have not selected a valid game")

    grid = np.random.choice(initial_state_options, n*n, p=initial_state_probabilities).reshape(n, n)

    return grid



if __name__ == '__main__':
    test = generate_world(100, 0.0001, 1)

    fig, ax = plt.subplots()
    img = ax.imshow(test, interpolation='nearest')
    plt.show()

