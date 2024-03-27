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





fig, ax = plt.subplots()
img = ax.imshow(trial_world, interpolation='nearest', vmin=0)

# Function to update the animation frames
def update(frame, img, trial_world, trial_kernel):
    img.set_array(game_options[game_selection](frame, img, trial_world, trial_kernel))
    return img,

# Function to calculate the sum of all cells in the final frame
def calculate_final_sum(frame, trial_world, trial_kernel):
    final_frame = game_options[game_selection](frame, trial_world, trial_kernel)
    return final_frame.sum()

ani = animation.FuncAnimation(fig, update, fargs=(img, trial_world, trial_kernel), frames=50, interval=50,
                              repeat=False, save_count=1000)

ax.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)

# Run the animation
plt.show()

# Calculate the sum of all cells in the final frame
final_sum = calculate_final_sum(49, trial_world, trial_kernel)
print("Sum of all cells in the final frame:", final_sum)

