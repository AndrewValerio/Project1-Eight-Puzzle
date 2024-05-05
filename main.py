from math import ceil
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
        print_solution(result, algorithm_option)
    else:
        print("No solution found.")

def print_solution(node, option):
    # This function will trace back from the goal node to the initial node
    path = []
    while node.parent is not None:  # Trace back the path
        path.append(node)
        node = node.parent
    path.append(node)
    path.reverse()  # Reverse the path to get the correct order
    for node in path:
        if node.action != None and node.problem.goal_test != True:
            if option == "1":
                print("The best state to expand with g(n) = ", node.path_cost, " is ", node.action)  # Print each action in the path
            elif option == "2":
                h_n = node.misplaced_tile()
                print("The best state to expand with g(n) = ", node.path_cost, " and h(n) ", h_n , node.action)  # Print each action in the path
            elif option == "3":
                h_n = ceil(node.euclidean_distance())
                print("The best state to expand with g(n) = ", node.path_cost, " and h(n) ", h_n , node.action)  # Print each action in the path
        elif node.action == None:
            print("Expanding State")

  
        for row in node.state:
            print(' '.join(str(cell) for cell in row))
        if node.action != None:
            print("Expanding this node...")
        print("\n")

    print("GOOOOAAAAAAALLLLLLLLL")
    print("")

    print("To Solve this problem the search algorithm expanded a total of",node.problem.expanded_nodes,"nodes.")
    print("")
    print("The maximum number of nodes in the queue at any one time:",node.problem.max_queue,".")
    print("") 
    print("The depth of the goal node was",node.path_cost,".")
    print("") 

main()



