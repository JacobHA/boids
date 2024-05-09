# Papers:
- https://esajournals.onlinelibrary.wiley.com/doi/epdf/10.1002/ecs2.2447
- https://ai.stanford.edu/~ang/papers/icml00-irl.pdf

# Code: 
- https://github.com/qzed/irl-maxent/blob/master/

# Action Space:
- create a 2D grid for discretizing the trajectories of each flight into discrete actions.
- implemented movement in all 8 neighboring cells.
- grid size: 40 (rows/latitude) x 40 (cols/longitude) = 1640 total possible states
- action data is stored in `./action_space.csv`. Format: Gen = generation of the bird chain, Pair = replicate, Release = flight number, Action = ordered states that a flight traverses, arranged from start to finish.
