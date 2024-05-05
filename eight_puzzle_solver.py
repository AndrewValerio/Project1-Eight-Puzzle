from queue import *
import copy
import math

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0, problem=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.problem = problem
        
    def findStar(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == '*':
                    return i, j

    def get_children(self):
        nodes_children = []
        for move in [self.go_left(), self.go_right(), self.go_up(), self.go_down()]:
            if move is not None:
                nodes_children.append(move)
        return nodes_children

        # Now find out possible moves to do based on star_row and star_col

    #left
    def go_left(self):
        star_row, star_col = self.findStar()
        if star_col == 0:
            return None  # Can't move left from this position
        else:
            child_state = [list(row) for row in self.state]  # Create a copy of the current state
            child_state[star_row][star_col], child_state[star_row][star_col - 1] = child_state[star_row][star_col - 1], child_state[star_row][star_col]
            return Node(child_state, self, 'left', self.path_cost + 1, self.problem)

    #right 
    def go_right(self):
        star_row, star_col = self.findStar()
        if star_col == len(self.state[0]) - 1:
            return None  # Can't move right from this position
        else:
            child_state = [list(row) for row in self.state]  # Create a copy of the current state
            child_state[star_row][star_col], child_state[star_row][star_col + 1] = child_state[star_row][star_col + 1], child_state[star_row][star_col]
            return Node(child_state, self, 'right', self.path_cost + 1, self.problem)

    #up
    def go_up(self):
        star_row, star_col = self.findStar()
        if star_row == 0:
            return None  # Can't move up from this position
        else:
            child_state = [list(row) for row in self.state]  # Create a copy of the current state
            child_state[star_row][star_col], child_state[star_row - 1][star_col] = child_state[star_row - 1][star_col], child_state[star_row][star_col]
            return Node(child_state, self, 'up', self.path_cost + 1, self.problem)

    #down
    def go_down(self):
        star_row, star_col = self.findStar()
        if star_row == len(self.state) - 1:
            return None  # Can't move down from this position
        else:
            child_state = [list(row) for row in self.state]  # Create a copy of the current state
            child_state[star_row][star_col], child_state[star_row + 1][star_col] = child_state[star_row + 1][star_col], child_state[star_row][star_col]
            return Node(child_state, self, 'down', self.path_cost + 1, self.problem)
    
    def __lt__(self, other):        #fixes errors with PQ in UCS when compare node to node see ref for code error
        return self.path_cost < other.path_cost
    
    def misplaced_tile(self):
        if self.problem is not None:
            return self.problem.misplaced_tile(self)
        else:
            raise Exception("No problem instance associated with this node")

    def euclidean_distance(self):
        if self.problem is not None:
            return self.problem.euclidean_distance(self)
        else:
            raise Exception("No problem instance associated with this node")
    


class Problem:
    #goal_state = [[1, 2, 3], 
                  #[4, 5, 6], 
                  #[7, 8, '*']] #Moved goal_state here so i could access it with my test functiontion
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [
                        [1, 2, 3], 
                        [4, 5, 6], 
                        [7, 8, '*']
                        ]
        self.operators = []  # List of operators
        self.frontier = PriorityQueue()
        self.explored = set()
        self.max_queue = 0
        self.goal_node_depth = 0
        self.expanded_nodes = 0


    def goal_test(self, state):
        return state == self.goal_state

    def misplaced_tile(self, node):
        state = node.state  # Access the state attribute of the Node object
        misplaced = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != self.goal_state[i][j] and state[i][j] != '*':
                    misplaced += 1
        return misplaced
    
    def euclidean_distance(self, node):
        state = node.state
        distance = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != '*':
                    current_position = (i, j)
                    goal_position = self.find_goal_position(state[i][j])
                    current_distance = math.sqrt((goal_position[0] - current_position[0])**2 + (goal_position[1] - current_position[1])**2)
                    #print(f"Tile: {state[i][j]}, Current_position: {current_position}, Current Distance: {current_distance}, Goal Position: {goal_position}")
                    distance += current_distance
        return distance

    
    def find_goal_position(self, value):
        for i in range(len(self.goal_state)):
            for j in range(len(self.goal_state[i])):
                if self.goal_state[i][j] == value:
                    #print(f"Found value {value} at position ({i}, {j}) in goal state")
                    return i, j
    
def get_initial_state():
    print("Enter your puzzle, use a * to represent the blank\n")
    initial_state = []
    for i in range(3):
        row_input = input("Enter the {} row with three numbers, use space or tabs between numbers: ".format(["first", "second", "third"][i])).strip()
        row = row_input.split()
        row = [int(num) if num.isdigit() else num for num in row]  # Convert numbers to integers
        initial_state.append(row)
    return initial_state

def uniform_cost_search(problem):
    node = Node(problem.initial_state, path_cost=0, problem=problem)
    frontier = PriorityQueue()
    frontier.put((0, node)) 
    explored = set() 

    while not frontier.empty():  
        _, node = frontier.get() 
        node.problem.max_queue += 1
        node.problem.expanded_nodes += 1 # because we expand whenever we pop a node
        if problem.goal_test(node.state):  
            # print("To Solve this problem the search algorithm expanded a total of",node.problem.expanded_nodes,"nodes.")
            # print("")
            # print("The maximum number of nodes in the queue at any one time:",node.problem.max_queue,".")
            # print("") 
            # print("The depth of the goal node was",node.path_cost,".")
            # print("") 
            return node 
        
        explored.add(tuple(map(tuple, node.state)))  
        for child in node.get_children(): 
            child_state_tuple = tuple(map(tuple, child.state))
            if child_state_tuple not in explored and not any(child_state_tuple == tuple(map(tuple, n[1].state)) for n in frontier.queue):
                frontier.put((child.path_cost, child))
                node.problem.goal_node_depth += 1
            else:
                for f in list(frontier.queue):
                    if child_state_tuple == tuple(map(tuple, f[1].state)) and f[1].path_cost > child.path_cost:
                        frontier.queue.remove(f)
                        frontier.put((child.path_cost, child)) 
                        break
    print("No solution.")
    return None

def a_star_search(problem, heuristic):
    # This method for the A* search algorithm
    # pass the type of heuristic (Misplaced tile or Elucidean Distance)
    # A8 is just uniform cost search, but uses g
    node = Node(problem.initial_state, path_cost=0, problem=problem)
    frontier = PriorityQueue()
    frontier.put((heuristic, node)) 
    explored = set() 

    while not frontier.empty():
        _, node = frontier.get()
        node.problem.max_queue += 1
        node.problem.expanded_nodes += 1 # because we expand whenever we pop a node
        if problem.goal_test(node.state):
            return node

        explored.add(tuple(map(tuple, node.state)))
        for child in node.get_children():
            child_state_tuple = tuple(map(tuple, child.state))
            if child_state_tuple not in explored and not any(child_state_tuple == tuple(map(tuple, n[1].state)) for n in frontier.queue):
                frontier.put((child.path_cost + heuristic(child), child))
                node.problem.goal_node_depth += 1
            else:
                for f in list(frontier.queue):
                    if child_state_tuple == tuple(map(tuple, f[1].state)) and f[1].path_cost > child.path_cost:
                        frontier.queue.remove(f)
                        frontier.put((child.path_cost + heuristic(child), child))
                        break

    return None

# formats our problem for printing 
def print_formatted_output(state):
    for row in state:
        print(" ".join(str(cell) for cell in row))

def print_solution_path(goal_state):
    path_list = []
    current_state = goal_state

    while current_state is not None:
        path_list.append(current_state)
        current_state = current_state.parent
    path_list.reverse()  
    print("Solution Path:")
    for node in path_list:
        print_formatted_output(node.state)  
        print("")




            


