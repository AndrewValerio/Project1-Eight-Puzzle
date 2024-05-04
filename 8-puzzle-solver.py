from queue import *
import copy
import math

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        
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
            return Node(child_state, self, 'left', self.path_cost + 1)

    #right 
    def go_right(self):
        star_row, star_col = self.findStar()
        if star_col == len(self.state[0]) - 1:
            return None  # Can't move right from this position
        else:
            child_state = [list(row) for row in self.state]  # Create a copy of the current state
            child_state[star_row][star_col], child_state[star_row][star_col + 1] = child_state[star_row][star_col + 1], child_state[star_row][star_col]
            return Node(child_state, self, 'right', self.path_cost + 1)

    #up
    def go_up(self):
        star_row, star_col = self.findStar()
        if star_row == 0:
            return None  # Can't move up from this position
        else:
            child_state = [list(row) for row in self.state]  # Create a copy of the current state
            child_state[star_row][star_col], child_state[star_row - 1][star_col] = child_state[star_row - 1][star_col], child_state[star_row][star_col]
            return Node(child_state, self, 'up', self.path_cost + 1)

    #down
    def go_down(self):
        star_row, star_col = self.findStar()
        if star_row == len(self.state) - 1:
            return None  # Can't move down from this position
        else:
            child_state = [list(row) for row in self.state]  # Create a copy of the current state
            child_state[star_row][star_col], child_state[star_row + 1][star_col] = child_state[star_row + 1][star_col], child_state[star_row][star_col]
            return Node(child_state, self, 'down', self.path_cost + 1)
    
    def __lt__(self, other):        #fixes errors with PQ in UCS when compare node to node see ref for code error
        return self.path_cost < other.path_cost
    
    def euclidean_distance(self):
        distance = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] != '*':
                    current_position = (i, j)
                    goal_position = self.find_goal_position(self.state[i][j])
                    distance += math.sqrt((goal_position[0] - current_position[0])**2 + (goal_position[1] - current_position[1])**2)
        return distance
    
    def find_goal_position(self, value):
        for i in range(len(Problem.goal_state)):
            for j in range(len(Problem.goal_state[i])):
                if Problem.goal_state[i][j] == value:
                    return i, j

def test():
    # Initial state
    initial_state = [['*', 1, 2], [3, 4, 5], [6, 7, 8]]
    node = Node(initial_state)
    print("Initial state: ", node.state)

    # Test find_star
    star_row, star_col = node.findStar()
    print("Star position: ", (star_row, star_col))
    assert (star_row, star_col) == (0, 0), "Expected (0, 0), but got ({}, {})".format(star_row, star_col)

    # Test go_right
    right_node = node.go_right()
    print("State after going right: ", right_node.state)
    assert right_node.state == [[1, '*', 2], [3, 4, 5], [6, 7, 8]], "Expected [[1, '*', 2], [3, 4, 5], [6, 7, 8]], but got {}".format(right_node.state)

    # Test go_down
    down_node = node.go_down()
    print("State after going down: ", down_node.state)
    assert down_node.state == [[3, 1, 2], ['*', 4, 5], [6, 7, 8]], "Expected [[3, 1, 2], ['*', 4, 5], [6, 7, 8]], but got {}".format(down_node.state)

    # Test get_children
    children = node.get_children()
    print("Number of children: ", len(children))
    assert len(children) == 2, "Expected 2 children, but got {}".format(len(children))

    print("All tests passed!")

#test()

class Problem:
    goal_state = [[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, '*']] #Moved goal_state here so i could access it with my test functiontion
    def __init__(self, initial_state):
        self.initial_state = initial_state
        # self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, '*']]
        self.operators = []  # List of operators
        self.frontier = PriorityQueue()
        self.explored = set()

    def goal_test(self, state):
        return state == self.goal_state

    def misplaced_tile(self, state):
        misplaced = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != self.goal_state[i][j] and state[i][j] != '*':
                    misplaced += 1
        return misplaced
    
def get_initial_state():
    print("Enter your puzzle, use a zero to represent the blank\n")
    initial_state = []
    for i in range(3):
        row_input = input("Enter the {} row with three numbers, use space or tabs between numbers: ".format(["first", "second", "third"][i])).strip()
        row = row_input.split()
        initial_state.append(row)
    return initial_state

def uniform_cost_search(problem):
    node = Node(problem.initial_state, path_cost=0)
    frontier = PriorityQueue()
    frontier.put((0, node)) 
    explored = set() 

    while not frontier.empty():  
        _, node = frontier.get()  
        if problem.goal_test(node.state):  
            return node 

        explored.add(tuple(map(tuple, node.state)))  
        for child in node.get_children(): 
            child_state_tuple = tuple(map(tuple, child.state))
            if child_state_tuple not in explored and not any(child_state_tuple == tuple(map(tuple, n[1].state)) for n in frontier.queue):
                frontier.put((child.path_cost, child))  
            else:
                for f in list(frontier.queue):
                    if child_state_tuple == tuple(map(tuple, f[1].state)) and f[1].path_cost > child.path_cost:
                        frontier.queue.remove(f)
                        frontier.put((child.path_cost, child)) 
                        break

    return None #

def test_uniform_cost_search():
    # Test 1
    initial_state_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, '*', 8]
    ]

    problem_1 = Problem(initial_state_1)  
    result_1 = uniform_cost_search(problem_1)
    if result_1 and result_1.state == Problem.goal_state:
        print("UCS Test 1 Passed")
    else:
        print("UCS Test 1 Failed")

    # Test 2
    initial_state_2 = [
        [1, '*', 3],
        [4, 2, 5],
        [7, 8, 6]
    ]

    problem_2 = Problem(initial_state_2)
    result_2 = uniform_cost_search(problem_2)
    if result_2 and result_2.state == Problem.goal_state:
        print("UCS Test 2 Passed")
    else:
        print("UCS Test 2 Failed")

#test_uniform_cost_search()

def misplaced_test():
    initial_state = [['*', 1, 2], [3, 4, 5], [6, 7, 8]]
    problem = Problem(initial_state)
    misplaced_tiles = problem.misplaced_tile(initial_state)
    print("Misplaced tiles:", misplaced_tiles)

#misplaced_test()


def test_euclidean_distance():
    # Test 1
    initial_state_1 = [
        ['*', 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    node_1 = Node(initial_state_1)
    calculated_distance_1 = node_1.euclidean_distance()
    expected_distance_1 = math.sqrt(8) + 8
    print("Calculated distance 1: ", calculated_distance_1)
    print("Expected distance 1: ", expected_distance_1)
    assert abs(calculated_distance_1 - expected_distance_1) < .6, "Test 1 Failed"

    # Test 2
    initial_state_2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, '*']
    ]
    node_2 = Node(initial_state_2)
    calculated_distance_2 = node_2.euclidean_distance()
    expected_distance_2 = 0  # All tiles are in their goal positions
    print("Calculated distance 2: ", calculated_distance_2)
    print("Expected distance 2: ", expected_distance_2)
    assert abs(calculated_distance_2 - expected_distance_2) < .6, "Test 2 Failed"

    print("All tests passed!")

test_euclidean_distance()

def a_star_search(problem, heuristic):
    # This method for the A* search algorithm
    # pass the type of heuristic (Misplaced tile or Elucidean Distance)
    # A8 is just uniform cost search, but uses g
    pass


def main():
    print("Welcome to the 862331611 8 puzzle solver.\n")
    print("Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n") 
    number_option = input("Your choice:\n")
    if number_option == '2':
        state = get_initial_state()
        problem = Problem(state)
        print("\n")
    elif number_option == '1':
        state = [[1, 2, 3], [4, 5, 6], [7, '*', 8]]
        problem = Problem(state)
        print("\n")
    
    print("Enter your choice of algorithm: \n")
    print("1 for uniform cost search\n")
    print("2 for A* with the Misplaced Tile heuristic\n")
    print("3 for A* with the Euclidean Distance heuristic \n")
    algorithm_option = input("\n")

    if algorithm_option == "1":
        pass
    elif algorithm_option == "2":
        pass
    elif algorithm_option == "3":
        pass
    

#main()



            


