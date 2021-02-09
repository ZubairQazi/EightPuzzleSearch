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


main()
