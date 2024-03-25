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
from extended_kernel import extended_kernel

from conway_rules import conway
from smooth_rules import smooth
from lenia_rules import lenia


matplotlib.rcParams['animation.ffmpeg_path'] = '/Users/maxharvey/anaconda/bin/ffmpeg'


world_size = 200
life_parameter = 0.9

#trial_world = generate_world(world_size, life_parameter, 0)
#trial_world = generate_world(world_size, life_parameter, 2)
#trial_world = trilobite(100, 13)



#trial_kernel = conway_kernel()
#trial_kernel = smooth_kernel()
#trial_kernel = lenia_kernel()
#trial_kernel = extended_kernel[0]

kernel_channel1 = extended_kernel()[0]  # Define kernel for channel 1
kernel_channel2 = extended_kernel()[1]  # Define kernel for channel 2

fig, ax = plt.subplots()

# Define two different colormaps for representing two channels
cmap_channel1 = matplotlib.colors.ListedColormap(['black', 'blue'])  # Define colors for channel 1
cmap_channel2 = matplotlib.colors.ListedColormap(['black', 'red'])  # Define colors for channel 2

# Plot the two channels separately
img_channel1 = ax.imshow(trial_world[..., 0], cmap=cmap_channel1, interpolation='nearest', vmin=0, vmax=1)
img_channel2 = ax.imshow(trial_world[..., 1], cmap=cmap_channel2, interpolation='nearest', vmin=0, vmax=1,
                         alpha=0.5)  # Set alpha for transparency

# Combine both channels in a single plot
img_combined = [img_channel1, img_channel2]


def update(frame, *fargs):
    for i, img in enumerate(img_combined):
        fargs[i].set_array(fargs[i].get_array())  # Update data for each channel

    # Apply different kernels to different channels
    new_world_channel1 = lenia(frame, *fargs[:2], trial_world[..., 0], kernel_channel1)
    new_world_channel2 = conway(frame, *fargs[:2], trial_world[..., 1], kernel_channel2)

    trial_world[..., 0] = new_world_channel1  # Update world for channel 1
    trial_world[..., 1] = new_world_channel2  # Update world for channel 2


ani = animation.FuncAnimation(fig, update,
                              fargs=(img_channel1, img_channel2, trial_world, kernel_channel1, kernel_channel2),
                              frames=250, interval=50,
                              repeat=False, save_count=250)



writer_video = animation.FFMpegWriter(fps=30)
#ani.save('Lenia_kernels_video.mp4', writer=writer_video, dpi=150)

plt.show()

