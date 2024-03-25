"""
This Python script generates an animation of the Game of Life, a cellular automaton devised by the British mathematician John Horton Conway.

Imports:
- matplotlib.pyplot as plt: Module for plotting.
- matplotlib.animation as animation: Module for creating animations.
- build_world.generate_world: Function to generate the initial world state.
- build_kernel.generate_kernel: Function to generate kernels.
- smooth_life_kernel_test.smooth_kernel: Function to generate smooth kernels.
- conway.conway: Function implementing the original Conway's Game of Life rules.
- smooth.smooth: Function implementing smooth life rules.

Parameters:
- world_size (int): Size of the Game of Life world (typically a square grid).
- life_parameter (float): Initial probability of a cell being alive.
- trial_world (numpy.ndarray): Initial random world generated using generate_world.

Process:
1. Generates an initial random world using generate_world.
2. Generates a kernel using generate_kernel or smooth_kernel.
3. Sets up plotting.
4. Initializes an image object with the initial world state.
5. Creates an animation using FuncAnimation, updating the plot with the smooth function.
6. Runs the animation for 1000 frames with a 50-millisecond interval.
7. Displays the animation using plt.show().
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
import numpy as np
import scipy

from build_world import generate_world
from trilobite import trilobite

from conway_kernel import conway_kernel
from smooth_kernel import smooth_kernel
from lenia_kernel import lenia_kernel

from conway_rules import conway
from smooth_rules import smooth
from lenia_rules import lenia


matplotlib.rcParams['animation.ffmpeg_path'] = '/Users/maxharvey/anaconda/bin/ffmpeg'


world_size = 250
life_parameter = 0.4

#trial_world = generate_world(world_size, life_parameter, 0)
trial_world = generate_world(world_size, life_parameter, 2)
#trial_world = trilobite(100, 13)



#trial_kernel = conway_kernel()
#trial_kernel = smooth_kernel()
trial_kernel = lenia_kernel()


fig, ax = plt.subplots()
img = ax.imshow(trial_world, cmap='jet', interpolation='nearest', vmin=0)
ani = animation.FuncAnimation(fig, lenia, fargs=(img, trial_world, trial_kernel), frames=250, interval=25,
                              repeat=False, save_count=250)


plt.show()


writer_video = animation.FFMpegWriter(fps=15)
#ani.save('.mp4', writer=writer_video, dpi=300)

