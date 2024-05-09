import pandas as pd
from trajectory import Trajectory
from gridworld import cardinal_to_int_action

def load_data(file_name):
    data = pd.read_csv(file_name)
    return data

# Reorganize the data to "Trajectory" style with (s,a,s') tuples:
def reorganize_data(data, pair=None, generation=None, releases=None):
    action_lookup = pd.read_csv('action_lookup.csv')
    # Consider each "Release" column as a separate trajectory:
    if generation is not None:
        data = data[data['Gen'] == generation]
    if pair is not None:
        data = data[data['Pair'] == pair]
    if releases is None:
        releases = data['Release'].unique()

    trajectories = []
    for release_n, release in enumerate(releases):
        transitions = []
        # Filter the data for the current trajectory:
        traj_data = data[data['Release'] == release]
        # Iterate over the rows of the trajectory data:
        for i in traj_data.index[:-1]:
            # Get the current state, action and next state:
            s = traj_data['State'][i]

            # a = traj_data['Action'][i]
            # a = cardinal_to_int_action(a)
            s_prime = traj_data['State'][i+1]
            a_list = action_lookup[action_lookup['cell_id'] == s] == s_prime
            # Grab the only action that is True:
            a = a_list.iloc[0, 2:].idxmax()  # Assuming 'cell_id' is in the first column
            a_int = cardinal_to_int_action(a)
            # Append the tuple to the transitions list:
            transitions.append((s, a_int, s_prime))
        # Add the final state:
        if len(traj_data) > 0:
            # transitions.append((traj_data['State'].iloc[-1], 0, 0))
            trajectories.append(Trajectory(transitions))

    return trajectories

def get_all_trajectories():
    data = load_data('action_space.csv')
    trajs = []
    for pair in range(1,39):
        try:
            trajectory = reorganize_data(data, pair=pair, generation=5, releases=list(range(9,13)))
            # Check if the trajectory is not empty:
            if len(trajectory) > 0:
                trajs += trajectory
        except:
            pass
    
    return trajs
