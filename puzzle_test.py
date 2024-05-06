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
    # Test 1: Trivial
    initial_state_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, '*']
    ]

    problem_1 = Problem(initial_state_1)  
    result_1 = uniform_cost_search(problem_1)
    if result_1 and result_1.state == problem_1.goal_state:
        print("UCS Trivial Test Passed")
        print("")
    else:
        print("UCS Trivial Test Failed")

    # Test 2: Easy
    initial_state_2 = [
        [1, 2, '*'],
        [4, 5, 3],
        [7, 8, 6]
    ]

    problem_2 = Problem(initial_state_2)
    result_2 = uniform_cost_search(problem_2)
    if result_2 and result_2.state == problem_2.goal_state:
        print("UCS Easy Test Passed")
        print("")
    else:
        print("UCS Easy Test Failed")

    # Test 3: Doable
    initial_state_3 = [
        ['*', 1, 2],
        [4, 5, 3],
        [7, 8, 6]
    ]

    problem_3 = Problem(initial_state_3)
    result_3 = uniform_cost_search(problem_3)
    if result_3 and result_3.state == problem_3.goal_state:
        print("UCS Doable Test Passed")
        print("")
    else:
        print("UCS Doable Test Failed")

    # Test 4: Oh Boy
    initial_state_4 = [
        [8, 7, 1],
        [6, '*', 2],
        [5, 4, 3]
    ]

    problem_4 = Problem(initial_state_4)
    result_4 = uniform_cost_search(problem_4)
    if result_4 and result_3.state == problem_4.goal_state:
        print("UCS Oh Boy Test Passed")
        print("")
    else:
        print("UCS Oh Boy Test Failed")


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

