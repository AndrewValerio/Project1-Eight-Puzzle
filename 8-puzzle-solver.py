from queue import *

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def get_children(self):
        # This method to generate the children of this node
        pass

class Problem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.operators = []  # List of operators
        self.frontier = PriorityQueue()
        self.explored_list = []

    def goal_test(self, state):
        # This method to check if the goal state has been reached
        pass

    def get_cost(self, state1, state2):
        # This method to get the cost of the transition from state1 to state2
        pass

def uniform_cost_search(problem):
    # This method for the uniform cost search algorithm

    # Template for function ----

    # function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
    # node ←a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    # frontier ← a priority queue ordered by PATH-COST, with node as the only element
    # explored ← an empty set
    # loop do
    # if EMPTY?(frontier ) then return failure
    # node ← POP(frontier ) /* chooses the lowest-cost node in frontier */
    # if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    # add node.STATE to explored
    # for each action in problem.ACTIONS(node.STATE) do
    # child ← CHILD-NODE(problem, node, action)
    # if child.STATE is not in explored or frontier then
    # frontier ← INSERT(child,frontier )
    # else if child.STATE is in frontier with higher PATH-COST then
    # replace that frontier node with child


    pass

def a_star_search(problem, heuristic):
    # This method for the A* search algorithm
    # pass the type of heuristic (Misplaced tile or Elucidean Distance)
    pass
