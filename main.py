from eight_puzzle_solver import *
from puzzle_test import *

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

print("Testing node moving")

test_node_moves()

print("Testing Uniform Cost Search")

print()

test_uniform_cost_search()

print("Testing Misplaced Tiles")

print()

misplaced_test()

print("Testing Euclidean Distance")

print()

test_euclidean_distance()