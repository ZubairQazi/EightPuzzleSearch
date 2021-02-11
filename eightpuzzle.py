import copy
from node import Node

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]
# stores seen puzzles to avoid duplicates
seen = []


def main():
    default_puzzle = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 0, 8]]

    puzzle, heuristic = print_menu()

    root = Node(puzzle, 0, 0)

    print('Expanding state')
    print_puzzle(root)

    result = search(root, heuristic)
    if result is not None:
        print('Solution found at depth: ', result.depth)
    else:
        print('No solution found after 50000 expansions')


# general search function
def search(root: Node, heuristic):
    nodes = [root]
    expansion_count = max_nodes = 0

    while len(nodes) != 0 and expansion_count < 50000:
        node = nodes.pop(0)
        if node.puzzle == goal:
            print('Nodes expanded:', expansion_count)
            print('Max number of nodes in queue: ', max_nodes)
            return node

        # update the queue
        nodes = update_queue(node, nodes, heuristic)
        # update counters
        expansion_count += 1
        if len(nodes) > max_nodes:
            max_nodes = len(nodes)

    print('No solution found')
    return None


# Expand the node and update the queue(nodes)
def update_queue(node, nodes, heuristic):

    # stores seen puzzles to avoid duplicates
    global seen

    # add children of node to queue

    child = copy.deepcopy(node)
    # first expansion
    child = move_up(child)
    if child is not None:
        child.depth = node.depth + 1
        # uniform cost
        if heuristic == '1':
            child.cost = child.depth + 0
        # misplaced tile
        if heuristic == '2':
            child.cost = child.depth + misplaced_heuristic(child)
        # manhattan distance
        if heuristic == '3':
            child.cost = child.depth + manhattan_heuristic(child)

        # check if the same cost & puzzle have been seen before
        if (child.cost, child.puzzle) not in seen:
            nodes.append(child)
            seen.append((child.cost, child.puzzle))

    child = copy.deepcopy(node)
    # second expansion
    child = move_down(child)
    if child is not None:
        child.depth = node.depth + 1
        # uniform cost
        if heuristic == '1':
            child.cost = child.depth + 0
        # misplaced tile
        if heuristic == '2':
            child.cost = child.depth + misplaced_heuristic(child)
        # manhattan distance
        if heuristic == '3':
            child.cost = child.depth + manhattan_heuristic(child)

        # check if the same cost & puzzle have been seen before
        if (child.cost, child.puzzle) not in seen:
            nodes.append(child)
            seen.append((child.cost, child.puzzle))

    child = copy.deepcopy(node)
    # third expansion
    child = move_left(child)
    if child is not None:
        child.depth = node.depth + 1
        # uniform cost
        if heuristic == '1':
            child.cost = child.depth + 0
        # misplaced tile
        if heuristic == '2':
            child.cost = child.depth + misplaced_heuristic(child)
        # manhattan distance
        if heuristic == '3':
            child.cost = child.depth + manhattan_heuristic(child)

        # check if the same cost & puzzle have been seen before
        if (child.cost, child.puzzle) not in seen:
            nodes.append(child)
            seen.append((child.cost, child.puzzle))

    child = copy.deepcopy(node)
    # fourth expansion
    child = move_right(child)
    if child is not None:
        child.depth = node.depth + 1
        # uniform cost
        if heuristic == '1':
            child.cost = child.depth + 0
        # misplaced tile
        if heuristic == '2':
            child.cost = child.depth + misplaced_heuristic(child)
        # manhattan distance
        if heuristic == '3':
            child.cost = child.depth + manhattan_heuristic(child)

        # check if the same cost & puzzle have been seen before
        if (child.cost, child.puzzle) not in seen:
            nodes.append(child)
            seen.append((child.cost, child.puzzle))

    # sort the list based on the cost g(n) + h(n)
    nodes = sorted(nodes, key=lambda n: n.cost)

    # output the node to be expanded in the next iterations cost and puzzle
    print(f'We are expanding state with g(n) = {nodes[0].depth} and f(n) = {nodes[0].cost - nodes[0].depth}')
    print_puzzle(nodes[0])
    print()

    return nodes


'''
HEURISTIC FUNCTIONS
'''


# returns the number of misplaced tiles
def misplaced_heuristic(node: Node):
    misplaced_count = 0
    for i, row in enumerate(node.puzzle):
        for j, val in enumerate(row):
            # account for the blank tile
            if val != goal[i][j] and val != 0:
                misplaced_count += 1

    return misplaced_count


# returns the manhattan heuristic evaluation
def manhattan_heuristic(node: Node):
    manhattan_sum = 0
    for i, row in enumerate(node.puzzle):
        for j, val in enumerate(row):
            # return index of value in goal state
            r, c = find(goal, val)
            # ensures that the value was found in the puzzle
            if all(v != -1 for v in (r, c)) and val != 0:
                # sums the manhattan distance of each tile
                manhattan_sum += (abs(r - i) + abs(c - j))

    return manhattan_sum


'''
TILE MOVING FUNCTIONS
'''


def move_up(node: Node):
    r, c = find(node.puzzle, 0)
    # if not applicable, return null
    if r == 2:
        return None

    # swap the blank tile with the one above
    node.puzzle[r][c], node.puzzle[r + 1][c] = node.puzzle[r + 1][c], node.puzzle[r][c]

    return node


def move_down(node: Node):
    r, c = find(node.puzzle, 0)
    # if not applicable, return null
    if r == 0:
        return None

    # swap the blank tile with the one above
    node.puzzle[r][c], node.puzzle[r - 1][c] = node.puzzle[r - 1][c], node.puzzle[r][c]

    return node


def move_left(node: Node):
    r, c = find(node.puzzle, 0)
    # if not applicable, return null
    if c == 2:
        return None

    # swap the blank tile with the one above
    node.puzzle[r][c], node.puzzle[r][c + 1] = node.puzzle[r][c + 1], node.puzzle[r][c]

    return node


def move_right(node: Node):
    r, c = find(node.puzzle, 0)
    # if not applicable, return null
    if c == 0:
        return None

    # swap the blank tile with the one above
    node.puzzle[r][c], node.puzzle[r][c - 1] = node.puzzle[r][c - 1], node.puzzle[r][c]

    return node


'''
HELPER FUNCTIONS
'''


# returns index (row, col) of value in puzzle
def find(puzzle, val):
    for i, row in enumerate(puzzle):
        for j, col in enumerate(row):
            if col == val:
                return i, j

    # returns -1 if value is not found
    return -1, -1


# pretty print the node's puzzle
def print_puzzle(node: Node):
    for row in node.puzzle:
        # print each element in the row separated by space
        print(' '.join([str(x) for x in row]))


def print_menu():
    puzzle = []

    print('Welcome to Zubair\'s 8-puzzle solver')
    print('Enter your puzzle, use a zero for the blank')

    puzzle.append((input('Enter the first row, separate with spaces: ')).split(' '))
    puzzle.append((input('Enter the second row, separate with spaces: ')).split(' '))
    puzzle.append((input('Enter the third row, separate with spaces: ')).split(' '))

    # convert each element in the puzzle to an integer
    puzzle = [[int(val) for val in row] for row in puzzle]

    print('\nEnter the desired algorithm')
    print('\t1. Uniform Cost Search')
    print('\t2. A* with Misplaced Tile')
    print('\t3. A* with Manhattan Distance\n')

    heuristic = input()

    return puzzle, heuristic


main()