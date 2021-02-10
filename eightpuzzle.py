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
    count = 0
    for i, row in enumerate(node.puzzle):
        for j, val in enumerate(row):
            if val != goal[i][j]:
                count += 1

    return count


# returns the
def manhattan_heuristic(node, val):
    # TODO: Implement manhattan heuristic
    return 0


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
