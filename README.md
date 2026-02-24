# CPSC 481 – Gridworld BFS
### Noah Scott

#### What is the state representation?

The state is represented as a tuple (row, col) corresponding to the agent’s position in the 2D Gridworld.
Each state uniquely identifies a cell in the grid.

##### The grid itself is a 2D list where:

- "S" = Start

- "G" = Goal

- "." = Traversable space

- "x" = Wall (blocked cell)

##### The BFS algorithm explores valid neighboring states (up, down, left, right) that are:

- Within grid bounds

- Not walls

- Not already visited

Parent pointers are stored in a dictionary to reconstruct the path once the goal is reached.



#### Why does BFS guarantee the shortest path in this grid?

Breadth-First Search (BFS) explores nodes level by level, meaning it first explores all states at distance 1 from the start, then distance 2, and so on.

Because:

- All moves in this grid have equal cost (each move = 1 step)

- BFS expands states in order of increasing depth

The first time the goal is reached, it must be via the shortest possible path in terms of number of steps.

Therefore, BFS guarantees the shortest path in an unweighted grid like this one.



#### Results

Path length (number of steps) = 6
Nodes expanded (number of states processed) = 9
