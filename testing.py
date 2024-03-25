"""
This demonstrates how three channels can successfully be broadcast over each other.
However, I think that this needs to be done a different way as all the channels are going to be
dependent upon each other
"""


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
import numpy as np

from build_world import generate_world
from trilobite import trilobite

from conway_kernel import conway_kernel
from smooth_kernel import smooth_kernel
from lenia_kernel import lenia_kernel
from extended_kernel import extended_kernel

from conway_rules import conway
from smooth_rules import smooth
from lenia_rules import lenia

matplotlib.rcParams['animation.ffmpeg_path'] = '/Users/maxharvey/anaconda/bin/ffmpeg'

world_size = 200
life_parameter = 0.9

trial_world = generate_world(world_size, life_parameter, 2)

trial_kernel1 = extended_kernel()[2]
trial_kernel2 = extended_kernel()[1]
trial_kernel3 = extended_kernel()[0]

fig, ax = plt.subplots()

img1 = ax.imshow(trial_world, cmap='Blues', interpolation='nearest', vmin=0, alpha=3)
ani1 = animation.FuncAnimation(fig, lenia, fargs=(img1, trial_world.copy(), trial_kernel1), frames=250, interval=50,
                               repeat=False, save_count=250)

img2 = ax.imshow(trial_world, cmap='Reds', interpolation='nearest', vmin=0, alpha=0.5)
ani2 = animation.FuncAnimation(fig, lenia, fargs=(img2, trial_world.copy(), trial_kernel2), frames=250, interval=50,
                               repeat=False, save_count=250)

img3 = ax.imshow(trial_world, cmap='Greens', interpolation='nearest', vmin=0, alpha=0.25)
ani3 = animation.FuncAnimation(fig, lenia, fargs=(img3, trial_world.copy(), trial_kernel3), frames=250, interval=50,
                               repeat=False, save_count=250)


plt.show()
