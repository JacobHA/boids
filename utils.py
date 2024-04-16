# Convert lists of [s,a,s',a',...] to a "Trajectories" object
from trajectory import Trajectory

def sa_to_sas_trajectories(sa_trajectories):
    """
    Convert a list of state-action-state-action-... sequences to a list of
    Trajectories.

    Args:
        data: The list of state-action-state-action-... sequences.

    Returns:
        A list of Trajectory objects.
    """
    trajectories = []
    for trajectory in sa_trajectories:
        transitions = [(trajectory[i], trajectory[i + 1], trajectory[i + 2]) for i in range(0, len(trajectory), 2)]
        
        # Add final state
        transitions.append((transitions[-1][2], 0, 0))

        trajectories.append(Trajectory(transitions))
    
    return trajectories

