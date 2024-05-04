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
        result = uniform_cost_search(problem)
    elif algorithm_option == "2":
        result = a_star_search(problem, problem.misplaced_tile)
    elif algorithm_option == "3":
        result = a_star_search(problem, problem.euclidean_distance) 

    if result is not None:
        print_solution(result)
    else:
        print("No solution found.")

def print_solution(node):
    # This function will trace back from the goal node to the initial node
    path = []
    while node.parent is not None:  # Trace back the path
        path.append(node)
        node = node.parent
    path.append(node)
    path.reverse()  # Reverse the path to get the correct order
    for node in path:
        print(node.action)  # Print each action in the path
        for row in node.state:
            print(' '.join(str(cell) for cell in row))
        print("\n")

main()


