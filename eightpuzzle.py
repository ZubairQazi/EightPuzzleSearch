from node import Node
import copy

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]


def main():
    default_puzzle = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 0, 8]]

    puzzle, heuristic = print_menu()

    root = Node(puzzle, 0, 0, [])
    result = search(root, heuristic)
    if result is not None:
        print('Solution found at depth: ', result.depth)
    else:
        print('No solution found')


# general search function
def search(root: Node, heuristic):
    nodes = [root]
    expansion_count = 0

    while len(nodes) != 0 and expansion_count < 50000:
        node = nodes.pop(0)
        if node.puzzle == goal:
            return node
        print_puzzle(node)
        print()
        nodes = update_queue(node, nodes, heuristic)
        expansion_count += 1

    print('No solution found')
    return None


def update_queue(node, nodes, heuristic):
    # TODO: Test queueing function

    # add children of node to queue
    child1 = copy.deepcopy(node)
    child1 = move_up(child1)
    if child1 is not None:
        child1.depth = node.depth + 1
        # uniform cost
        if heuristic == '1':
            child1.cost = child1.depth + 0
        # misplaced tile
        if heuristic == '2':
            child1.cost = child1.depth + misplaced_heuristic(child1)
        # manhattan distance
        if heuristic == '3':
            child1.cost = child1.depth + manhattan_heuristic(child1)
        nodes.append(child1)

    child2 = copy.deepcopy(node)
    child2 = move_down(child2)
    if child2 is not None:
        child2.depth = node.depth + 1
        # uniform cost
        if heuristic == '1':
            child2.cost = child2.depth + 0
        # misplaced tile
        if heuristic == '2':
            child2.cost = child2.depth + misplaced_heuristic(child2)
        # manhattan distance
        if heuristic == '3':
            child2.cost = child2.depth + manhattan_heuristic(child2)
        nodes.append(child2)

    child3 = copy.deepcopy(node)
    child3 = move_left(child3)
    if child3 is not None:
        child3.depth = node.depth + 1
        # uniform cost
        if heuristic == '1':
            child3.cost = child3.depth + 0
        # misplaced tile
        if heuristic == '2':
            child3.cost = child3.depth + misplaced_heuristic(child3)
        # manhattan distance
        if heuristic == '3':
            child3.cost = child3.depth + manhattan_heuristic(child3)
        nodes.append(child3)

    child4 = copy.deepcopy(node)
    child4 = move_right(child4)
    if child4 is not None:
        child4.depth = node.depth + 1
        # uniform cost
        if heuristic == '1':
            child4.cost = child4.depth + 0
        # misplaced tile
        if heuristic == '2':
            child4.cost = child4.depth + misplaced_heuristic(child4)
        # manhattan distance
        if heuristic == '3':
            child4.cost = child4.depth + manhattan_heuristic(child4)
        nodes.append(child4)

    # sort the list based on the cost
    nodes = sorted(nodes, key=lambda n: n.cost)
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
    # TODO: Move blank tile left if applicable
    r, c = find(node.puzzle, 0)
    # if not applicable, return null
    if c == 2:
        return None

    # swap the blank tile with the one above
    node.puzzle[r][c], node.puzzle[r][c + 1] = node.puzzle[r][c + 1], node.puzzle[r][c]

    return node


def move_right(node: Node):
    # TODO: Move blank tile right if applicable
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
    print('Enter the puzzle, use a zero for the blank')

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
