import pandas as pd
from trajectory import Trajectory
from gridworld import cardinal_to_int_action

def load_data(file_name):
    data = pd.read_csv(file_name)
    return data

# Reorganize the data to "Trajectory" style with (s,a,s') tuples:
def reorganize_data(data, pair=1):
    # Consider each "Release" column as a separate trajectory:
    data = data[data['Pair'] == pair]
    releases = data['Release'].unique()
    trajectories = []
    for release_n, release in enumerate(releases):
        transitions = []
        # Filter the data for the current trajectory:
        traj_data = data[data['Release'] == release]
        # Iterate over the rows of the trajectory data:
        for i in range(len(traj_data) - 1):
            # Get the current state, action and next state:
            s = traj_data['State'][i]
            a = traj_data['Action'][i]
            a = cardinal_to_int_action(a)
            s_prime = traj_data['State'][i+1]
            # Append the tuple to the transitions list:
            transitions.append((s, a, s_prime))
        # Add the final state:
        trajectories.append(Trajectory(transitions))

    return trajectories

if __name__ == "__main__":
    data = load_data('action_space.csv')
    trajectory = reorganize_data(data)
    print(trajectory)
