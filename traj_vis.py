# Visualize a Trajectory in the BirdWorld.

import os
import numpy as np
import matplotlib.pyplot as plt
from data_loader import get_all_trajectories, load_data, reorganize_data
from gridworld import BirdWorld
from trajectory import Trajectory


def visualize_trajectory(world, trajectory, show=True):
    """
    Visualize a trajectory in the given world.

    Args:
        world: The world in which the trajectory should be visualized.
        trajectory: The trajectory to visualize.
    """
    # Create a new figure:
    plt.figure()
    # Plot a grid of size world.width x world.height:
    grid = np.zeros((world.height, world.width))
    # plt.imshow(np.ones((world.width, world.height)), cmap='gray', origin='lower')
    # Get the states of the trajectory:
    states = list(trajectory.states())
    # Plot the trajectory:
    for i in range(len(states) - 1):
        # Get the current state and the next state:
        s = states[i]
        s_prime = states[i + 1]
        # Get the coordinates of the current state:
        y, x = world.state_index_to_point(s)
        # Get the coordinates of the next state:
        y_prime, x_prime = world.state_index_to_point(s_prime)

        # Draw an arrow from the current state to the next state:
        plt.arrow(y, x, 0.5*(y_prime - y), 0.5*(x_prime - x), head_width=0.1, head_length=0.05, fc='r', ec='r')

        # Add state to the grid:
        grid[x, y] = 1

    grid[x_prime, y_prime] = 1
    # Plot the trajectory:
    plt.imshow(1-grid, cmap='gray', origin='lower')
    # Show the plot:
    if show:
        plt.show()


def main():
    # Create a new world:
    world = BirdWorld(width=7, height=8)
    # Grab trajectories:
    data = load_data('action_space.csv')
    trajectory = reorganize_data(data)[0]
    # Visualize the trajectory:
    visualize_trajectory(world, trajectory)

def make_gif():
    world = BirdWorld(width=7, height=8)
    # Make a gif of all trajectories:
    trajectories = get_all_trajectories()
    os.makedirs('images', exist_ok=True)
    for i, trajectory in enumerate(trajectories):
        visualize_trajectory(world, trajectory, show=False)
        plt.savefig(f'images/trajectory_{i}.png')
        plt.close()

    import imageio
    images = []
    for i in range(len(trajectories)):
        images.append(imageio.imread(f'images/trajectory_{i}.png'))
    imageio.mimsave('trajectories.gif', images)

if __name__ == "__main__":
    # main()
    make_gif()