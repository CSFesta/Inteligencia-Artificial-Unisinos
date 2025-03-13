import math
# The maze
maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Start and end positions


# Class for representing a node (or cell) in the map
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
#manhattan
def f_manhattan(x1, y1, x2, y2):
    return x1-x2 + y1-y2

#euclidiana
def h_euclidiana(x1, y1, x2, y2):
  num1 = x2 - x1
  num2 = y2 - y1
  math.sqrt(pow(num1, 2) + pow(num2, 2))
  return 0 # TODO

#festa
def h_Festa(x1, y1, x2, y2):
    diff_x = x2 - x1
    diff_y = y2 - y1
    sum_diff = diff_x + diff_y
    
    if sum_diff <= 0:
        sum_diff = 1
    
    return diff_x + diff_y + math.log2(sum_diff)

#chebyshev
def h_chebyshev(x1,y1,x2,y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return max(dx, dy)

#octile
def h_octile(x1,y1,x2,y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    diagonal_cost = 1.4142135623730951  # Aproximadamente raiz quadrada de 2.
    return max(dx, dy) + (diagonal_cost - 2) * min(dx, dy)


# A-star algorithm
def astar(maze, start, end, heuristic):

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    iterations = 0
    while len(open_list) > 0:
        iterations += 1

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1], iterations # Return reversed path and the number of iterations to complete the algorithm

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # up, down, right, left

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            is_in_closed = False
            for closed_child in closed_list:
                if child == closed_child:
                    is_in_closed = True
                    break
            if is_in_closed:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = heuristic(child.position[0], child.position[1], end_node.position[0], end_node.position[1])
            child.f = child.g + child.h

            # Child is already in the open list
            is_in_open = False
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    is_in_open = True
                    break
            if is_in_open:
                continue

            # Add the child to the open list
            open_list.append(child)



start = (0, 0)
end = (7, 6)

path1 = astar(maze, start, end, h_euclidiana)
path2 = astar(maze, start, end, f_manhattan)
path3 = astar(maze, start, end, h_Festa)
path4 = astar(maze, start, end, h_chebyshev)
path5 = astar(maze, start, end, h_octile)

print(path1)
print(path2)
print(path3)
print(path4)
print(path5)

