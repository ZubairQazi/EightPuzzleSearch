from node import Node

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]


def main():
    puzzle = [[3, 2, 8],
              [4, 0, 5],
              [7, 1, 6]]

    root = Node(puzzle, 0, 0, [])
    # search(root, 0)
    print_puzzle(root)
    print()
    print_puzzle(move_left(root))


# general search function
def search(root: Node, heuristic):
    nodes = [root]

    while len(nodes) != 0:
        node = nodes.pop(0)
        if node == goal:
            return node
        nodes = update_queue(nodes, heuristic)

    print('No solution found')
    return -1


def update_queue(nodes, heuristic):
    # TODO: Implement queueing function
    return []


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
    # TODO: Move blank tile up if applicable
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


main()
