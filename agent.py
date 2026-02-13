# CPSC 481
# Noah Scott

from collections import deque



# Gridworld Map
# S = start, G = goal, . = empty, x = wall
Gridworld = [
    ["S", "x", "x", "."],
    [".", ".", "x", "."],
    ["x", ".", ".", "."],
    ["x", ".", "x", "G"]
]

# Config
starting_state = (0, 0)
goal_state = (3, 3)
agent_state = starting_state
agent_avatar = "A"
neighbors = deque()
neighbors.append(agent_state) 
visited = set()
parent = {}

while len(neighbors) > 0:
    vertex = neighbors.popleft()

    if not vertex in visited:
        visited.add(vertex)
        # direction = [up, down, left, right]
        directions = [(vertex[0] - 1, vertex[1]), (vertex[0] + 1, vertex[1]), (vertex[0], vertex[1] - 1), (vertex[0], vertex[1] + 1)]
        
        for dir in directions:
            if (dir[0] >= 0 and dir[0] < len(Gridworld)) and (dir[1] >= 0 and dir[1] < len(Gridworld[dir[0]])) and not dir in visited and Gridworld[dir[0]][dir[1]] != "x":
                neighbors.append(dir)
                parent[dir] = vertex
#    print(vertex)
path = []
path.append(goal_state)
path_pos = goal_state

while path_pos != starting_state:
    path.append(parent[path_pos])
    path_pos = parent[path_pos]
final_path = list(reversed(path))

for row in range (0, len(Gridworld)):
    for col in range (0, len(Gridworld[row])):
        print(Gridworld[row][col], " ", end="")
    print()
print()

curr = 0

for i in range (0, len(Gridworld)):
    for j in range (0, len(Gridworld[i])):
        if (i, j) == final_path[curr]:
            Gridworld[i][j] = str(curr)
            curr +=1
        print(Gridworld[i][j]," ",  end="")
    print()
