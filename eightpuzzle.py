from node import Node

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]


def main():
    puzzle = [[1, 2, 3],
              [4, 5, 6],
              [7, 0, 8]]

    root = Node(puzzle, 0, 0, [])
    search(root, 0)


# general search function
def search(root, heuristic):
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


# returns the number of misplaced tiles
def misplaced_heuristic(node):
    misplaced_count = 0
    for i, row in enumerate(node.puzzle):
        for j, val in enumerate(row):
            # account for the blank tile
            if val != goal[i][j] and val != 0:
                misplaced_count += 1

    return misplaced_count


# returns the manhattan heuristic evaluation
def manhattan_heuristic(node):
    manhattan_sum = 0
    for i, row in enumerate(node.puzzle):
        for j, val in enumerate(row):
            # return index of value in goal state
            r, c = find(goal, val)
            # ensures that the value was found in the puzzle
            if all(v != -1 for v in (r, c)):
                # sums the manhattan distance of each tile
                manhattan_sum += (abs(r - i) + abs(c - j))

    return manhattan_sum


# returns index (row, col) of value in puzzle
def find(puzzle, val):
    for i, row in enumerate(puzzle):
        for j, col in enumerate(row):
            if col == val:
                return i, j

    # returns -1 if value is not found
    return -1, -1


def move_up(node):
    # TODO: Move blank tile up if applicable
    return node


def move_down(node):
    # TODO: Move blank tile down if applicable
    return node


def move_left(node):
    # TODO: Move blank tile left if applicable
    return node


def move_right(node):
    # TODO: Move blank tile right if applicable
    return node


main()
