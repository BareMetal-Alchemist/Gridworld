# CPSC 481
# Noah Scott

# Gridworld Map
# G = goal, . = empty, x = wall
Gridworld = [
    [".", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "G"]
]

#Grid config
starting_x = 0
starting_y = 0

# Agent Config
agent_posX = 
agent_posY = 
agent_avatar = "A"


# Movement is limited to Up, Down, Left and Right
# Because of this we would adjust the agent's position 
# -1 or +1 in the x or y axis
# We are looking for breadth aka scanning the adjacent neighbors
# This limitation in movement is helpful when considering BFS


# Gameplay loop
while agent_position != "G":
    
