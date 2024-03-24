"""
This is the main file where experiments can be run from
"""

import matplotlib.pyplot as plt
from build_world import generate_world
from build_kernel import generate_kernel
from conway import conway
import matplotlib.animation as animation

from smooth_life_kernel_test import smooth_kernel
from smooth_life_rules_test import smooth


world_size = 250
life_parameter = 0.4
trial_world = generate_world(world_size, life_parameter, 0)


trial_kernel = generate_kernel()

kernel_1, kernel_2 = smooth_kernel()


fig, ax = plt.subplots()
img = ax.imshow(trial_world, interpolation='nearest')
ani = animation.FuncAnimation(fig, smooth, fargs=(img, trial_world, kernel_1, kernel_2), frames=1000, interval=50, save_count=50)


plt.show()

