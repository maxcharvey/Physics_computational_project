"""
Game of Life Animation Script

This Python script generates an animation of the Game of Life, a cellular automaton devised by the British mathematician John Horton Conway.

Imports:
- matplotlib.pyplot as plt: Module for plotting.
- matplotlib.animation as animation: Module for creating animations.
- build_world.generate_world: Function to generate the initial world state.
- conway_kernel, smooth_kernel, lenia_kernel, extended_kernel: Functions to generate kernels for different variations of the Game of Life.
- conway_rules, smooth_rules, lenia_rules, extended_rules: Functions implementing different rulesets for the Game of Life variations.

Parameters:
- world_size (int): Size of the Game of Life world (typically a square grid).
- life_parameter (float): Initial probability of a cell being alive.
- game_selection (int): Selection of the Game of Life variation:
                        0 = Conway's Game of Life
                        1 = Smooth Life
                        2 = Lenia
                        3 = Three-channel extended Lenia

Process:
1. Generates an initial random world using generate_world based on specified parameters.
2. Selects the appropriate kernel and rule functions based on the game selection.
3. Sets up plotting for animation.
4. Initializes an image object with the initial world state.
5. Creates an animation using FuncAnimation, updating the plot with the selected rule function.
6. Runs the animation for a specified number of frames with a given interval.
7. Displays the animation.

Note: Additional functionalities for saving videos are provided but commented out.

Author: Max Harvey
Date: 26-03-24
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

from build_world import generate_world

from conway_kernel import conway_kernel
from smooth_kernel import smooth_kernel
from lenia_kernel import lenia_kernel
from extended_kernel import extended_kernel

from conway_rules import conway
from smooth_rules import smooth
from lenia_rules import lenia
from extended_rules import extended

matplotlib.rcParams['animation.ffmpeg_path'] = '/Users/maxharvey/anaconda/bin/ffmpeg'

# Global variables that can be varied
world_size = 250 # This will produce an NxN grid for the games to run in
life_parameter = 0.1 # Controls how much initial life there is within the game


"""
This is the input through which you can select which game you would like to play:

0 = Conway's Game of Life
1 = Smooth Life
2 = Lenia
3 = Three channel extended Lenia
"""
game_selection = 3



# Some necessary lists pertaining to the game selection that is made
kernel_options = [conway_kernel(), smooth_kernel(), lenia_kernel(), extended_kernel()]
game_options = [conway, smooth, lenia, extended]

trial_world = generate_world(world_size, life_parameter, game_selection)
trial_kernel = kernel_options[game_selection]


# Generation of the animation
fig, ax = plt.subplots()
img = ax.imshow(trial_world, interpolation='nearest', vmin=0)
ani = animation.FuncAnimation(fig, game_options[game_selection], fargs=(img, trial_world, trial_kernel), frames=50, interval=50,
                              repeat=False, save_count=1000)
ax.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)

#cbar = fig.colorbar(img, ax=ax, orientation='vertical')
#cbar.set_ticks([0, 0.25, 0.5, 0.75, 1])  # Set ticks to desired values
#cbar.set_ticklabels(['0', '0.25', '0.5', '0.75', '1'])  # Set tick labels to desired values


#Going to make a secondary plot that looks at the behaviour of 6 systems side by side

#fig, (ax, ax1, ax2, ax3, ax4, ax5) = plt.subplots(figsize=(8,16), ncols=2, nrows=3)
#img =


# These parts can be used for saving videos if required
writer_video = animation.FFMpegWriter(fps=15)
#ani.save('Lenia_extended_test5.mp4', writer=writer_video, dpi=300)

# This displays the animation after any necessary saving has been completed
plt.show()

