"""
This is the main file where experiments can be run from
"""

import matplotlib.pyplot as plt
from build_world import generate_world
from build_kernel import generate_kernel
from conway import conway
import matplotlib.animation as animation


world_size = 100
life_parameter = 0.2
trial_world = generate_world(world_size, life_parameter, 0)
trial_kernel = generate_kernel()

fig, ax = plt.subplots()
img = ax.imshow(trial_world, interpolation='nearest')
ani = animation.FuncAnimation(fig, conway, fargs=(img, trial_world, trial_kernel), frames=100, interval=50, save_count=50)

plt.show()

