from queue import *
import copy

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost # path_cost is G(n), distance to goal is H(n)

    def findStar(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == '*':
                    return i, j

    def get_children(self):
        # This method to generate the children of this node
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
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, '*']]
        self.operators = []  # List of operators
        self.frontier = PriorityQueue()
        self.explored = set()

    def goal_test(self, state):
        return state == self.goal_state

    def get_distance_to_goal(self, state1, state2):
        # This method to get the distance the current state has to the goal
        pass

    def misplaced_tile(self, state):
        misplaced = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != self.goal_state[i][j]:
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
    # This method for the uniform cost search algorithm

    # Template for function ----

    # function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
    # node <-a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    # frontier <- a priority queue ordered by PATH-COST, with node as the only element
    # explored <- an empty set
    # loop do
    # if EMPTY?(frontier ) then return failure
    # node <- POP(frontier ) /* chooses the lowest-cost node in frontier */
    # if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    # add node.STATE to explored
    # for each action in problem.ACTIONS(node.STATE) do
    # child <- CHILD-NODE(problem, node, action)
    # if child.STATE is not in explored or frontier then
    # frontier <- INSERT(child,frontier )
    # else if child.STATE is in frontier with higher PATH-COST then
    # replace that frontier node with child

    # function findStar(puzzle)
    # puzzle is a 3x3 matrix

    # for i -> row
       # for j -> column

    # if  [i,j] == '*'

    # curent_puzzle = [
    #    [3,    6,    7],
    #    [5,    8,    *],
    #    [2     1,    4],
    # ]

    # returns [row, column] of the star [1, 2]

    # figuring out path cost
    

    pass

def misplaced_test():
    initial_state = [['*', 1, 2], [3, 4, 5], [6, 7, 8]]
    problem = Problem(initial_state)
    misplaced_tiles = problem.misplaced_tile(initial_state)
    print("Misplaced tiles:", misplaced_tiles)

#misplaced_test()

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
        state = [[1, 2, 3], ['*', 6, 7], [4, 5, 8]]
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

main()
