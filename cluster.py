#TODO: Need to revisit this script to see about creating more complex or well known/defined initial structures

import numpy as np
from scipy.stats import norm

def generate_world_cluster(n, p, game, cluster_prob, cluster_size):
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
    - cluster_prob: Float, specifying the probability of adding a cluster.
    - cluster_size: Integer, specifying the size of the cluster.

    Returns:
    - grid: 2D NumPy array, representing the initial state of the world/grid.

    Notes:
    - For Conway's Game of Life, the initial state consists of randomly distributed alive and dead cells based on the given probability.
    - For Smooth Life, Lenia, and Extended Lenia, the initial state is generated based on a normal distribution around the specified probability.
    - If an invalid game identifier is provided, a warning is printed, and Conway's Game of Life is assumed by default.
    """

    # Define normal distribution parameters for generating the initial state
    a = np.linspace(0, 1, 256)
    b = norm.pdf(a, p, 0.15)
    norm_normal = b / sum(b)

    if game <= 1:  # For Conway's game of life and smooth life
        probability_alive = p
        initial_state_options = [255, 0]
        initial_state_probabilities = [probability_alive, 1 - probability_alive]
        grid = np.random.choice(initial_state_options, n * n, p=initial_state_probabilities).reshape(n, n)

    elif game == 2:  # For Lenia
        initial_state_options = np.linspace(0, 1, 256)[::-1]
        initial_state_probabilities = norm_normal[::-1]
        grid = np.random.choice(initial_state_options, n * n, p=initial_state_probabilities).reshape(n, n)

    elif game == 3:  # For Extended Lenia where there will be 3 channels
        grid = np.empty((n, n, 3))
        for i in range(3):
            initial_state_options = np.linspace(0, 1, 256)[::-1]
            initial_state_probabilities = norm_normal[::-1]

            # Randomly add clusters with the specified probability
            if np.random.rand() < cluster_prob:
                # Generate cluster coordinates
                cluster_x = np.random.randint(0, n - cluster_size)
                cluster_y = np.random.randint(0, n - cluster_size)
                # Generate cluster values
                cluster_values = np.random.choice(initial_state_options, cluster_size * cluster_size, p=initial_state_probabilities).reshape(cluster_size, cluster_size)
                # Add the cluster to the grid
                grid[cluster_x:cluster_x+cluster_size, cluster_y:cluster_y+cluster_size, i] = cluster_values
            else:
                # Generate random values without clusters
                temp_grid = np.random.choice(initial_state_options, n * n, p=initial_state_probabilities).reshape(n, n)
                grid[:,:, i] = temp_grid

    else:
        probability_alive = p
        initial_state_options = [255, 0]
        initial_state_probabilities = [probability_alive, 1 - probability_alive]
        print("You have not selected a valid game")
        grid = np.random.choice(initial_state_options, n * n, p=initial_state_probabilities).reshape(n, n)

    return grid

