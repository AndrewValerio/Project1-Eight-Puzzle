from math import ceil
from eight_puzzle_solver import *

def test_node_moves():
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

def test_uniform_cost_search():
    # Test 1
    initial_state_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, '*', 8]
    ]

    problem_1 = Problem(initial_state_1)  
    result_1 = uniform_cost_search(problem_1)
    if result_1 and result_1.state == problem_1.goal_state:
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
    if result_2 and result_2.state == problem_2.goal_state:
        print("UCS Test 2 Passed")
    else:
        print("UCS Test 2 Failed")


def misplaced_test():
    initial_state = [['*', 1, 2], [3, 4, 5], [6, 7, 8]]
    problem = Problem(initial_state)
    misplaced_tiles = problem.misplaced_tile(initial_state)
    print("Misplaced tiles:", misplaced_tiles)


def test_euclidean_distance():
    # Test 1
    initial_state_1 = [
        ['*', 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    print("Initial State 1:")
    for row in initial_state_1:
        print(row)

    problem1 = Problem(initial_state_1)
    node_1 = Node(initial_state_1, problem=problem1)
    calculated_distance_1 = ceil(node_1.euclidean_distance())
    expected_distance_1 = ceil(math.sqrt(8) + 8)
    print("Calculated distance 1: ", calculated_distance_1)
    print("Expected distance 1: ", expected_distance_1)
    assert abs(calculated_distance_1 - expected_distance_1), "Test 1 Failed"

    # Test 2
    initial_state_2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, '*']
    ]

    print("Initial State 2:")
    for row in initial_state_2:
        print(row)
        
    problem2 = Problem(initial_state_2)
    node_2 = Node(initial_state_2, problem=problem2)
    calculated_distance_2 = node_2.euclidean_distance()
    expected_distance_2 = 0  # All tiles are in their goal positions
    print("Calculated distance 2: ", calculated_distance_2)
    print("Expected distance 2: ", expected_distance_2)
    assert abs(calculated_distance_2 - expected_distance_2), "Test 2 Failed"

    print("All tests passed!")

